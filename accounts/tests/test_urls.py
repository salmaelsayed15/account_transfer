from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import Account
from decimal import Decimal

class AccountsURLTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.account1 = Account.objects.create(account_number="123", account_holder_name="Alice", balance=Decimal('500.00'))
    
    def test_account_list_url(self):
        """Test that the account list URL is accessible."""
        response = self.client.get(reverse('account-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/account_list.html')
    
    def test_account_detail_url(self):
        """Test the account detail page loads correctly."""
        response = self.client.get(reverse('account-detail', args=['123']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Alice")
        self.assertTemplateUsed(response, 'accounts/account_detail.html')

    def test_transfer_funds_url(self):
        """Test the transfer funds form page loads correctly."""
        response = self.client.get(reverse('transfer-funds'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/transfer_form.html')
