from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from accounts.models import Account
from decimal import Decimal
import csv
import io
from django.contrib.messages import get_messages


class AccountViewTest(TestCase):
    
    def setUp(self):
        """Setup initial accounts for testing"""
        self.account1 = Account.objects.create(account_number="123", account_holder_name="Alice", balance=Decimal("500.00"))
        self.account2 = Account.objects.create(account_number="456", account_holder_name="Bob", balance=Decimal("300.00"))

    def test_account_list_view(self):
        """Test that the account list page returns 200 OK and includes accounts"""
        response = self.client.get(reverse('account-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Alice")
        self.assertContains(response, "Bob")

    def test_account_detail_view(self):
        """Test that the account detail page shows correct account data"""
        response = self.client.get(reverse('account-detail', args=["123"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Alice")
        self.assertContains(response, "123")
        self.assertContains(response, "500.00")

    def test_transfer_funds_success(self):
        """Test transferring funds successfully between accounts"""
        response = self.client.post(reverse('transfer-funds'), {
            'from_account': '123',
            'to_account': '456',
            'amount': '100.00'
        })
        self.assertRedirects(response, reverse('account-list'))

        self.account1.refresh_from_db()
        self.account2.refresh_from_db()

        self.assertEqual(self.account1.balance, Decimal("400.00"))  # Reduced
        self.assertEqual(self.account2.balance, Decimal("400.00"))  # Increased

    def test_transfer_funds_insufficient_balance(self):
        """Test that transferring funds fails for insufficient balance"""
        response = self.client.post(reverse('transfer-funds'), {
            'from_account': '456',
            'to_account': '123',
            'amount': '400.00'  # Bob only has 300.00
        })
        self.assertRedirects(response, reverse('transfer-funds'))

        self.account1.refresh_from_db()
        self.account2.refresh_from_db()

        self.assertEqual(self.account1.balance, Decimal("500.00"))
        self.assertEqual(self.account2.balance, Decimal("300.00"))
    

    def test_import_invalid_file_type(self):
        xml_data = "<accounts><account><id>1</id><name>John Doe</name><balance>1000</balance></account></accounts>"
        xml_file = SimpleUploadedFile("accounts.xml", xml_data.encode("utf-8"), content_type="application/xml")

        response = self.client.post(reverse('import-accounts'), {
            'file': xml_file,
            'file_type': 'xml',
        })

        # Check for 200 OK
        self.assertEqual(response.status_code, 200)

        # Capture messages
        messages = list(get_messages(response.wsgi_request))
        
        # Verify the error message
        self.assertTrue(any("File type xml is not supported." in message.message for message in messages))

