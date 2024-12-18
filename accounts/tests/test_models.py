from django.test import TestCase
from accounts.models import Account
from decimal import Decimal

class AccountModelTest(TestCase):

    def setUp(self):
        # Set up sample data
        Account.objects.create(account_number="123456789", account_holder_name="John Doe", balance=Decimal("100.00"))
    
    def test_account_creation(self):
        """Test creating an account"""
        account = Account.objects.get(account_number="123456789")
        self.assertEqual(account.account_holder_name, "John Doe")
        self.assertEqual(account.balance, Decimal("100.00"))
    
    def test_account_str_method(self):
        """Test the string representation of the Account"""
        account = Account.objects.get(account_number="123456789")
        self.assertEqual(str(account), "John Doe - 123456789")
