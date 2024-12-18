from django.core.management import call_command
from django.test import TestCase
from io import StringIO
from accounts.models import Account
from decimal import Decimal

class ImportAccountsCommandTest(TestCase):

    def test_import_accounts_command(self):
        """Test importing accounts from a CSV file"""
        csv_data = """ID,Name,Balance
123,John Doe,100.00
456,Jane Doe,200.00"""
        
        # Use StringIO to simulate a CSV file
        out = StringIO()
        with open('test_accounts.csv', 'w') as file:
            file.write(csv_data)

        call_command('import_accounts', 'test_accounts.csv', stdout=out)

        # Check accounts were created
        self.assertEqual(Account.objects.count(), 2)
        account1 = Account.objects.get(account_number="123")
        self.assertEqual(account1.account_holder_name, "John Doe")
        self.assertEqual(account1.balance, Decimal("100.00"))
