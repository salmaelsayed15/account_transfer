from django.test import TestCase
from django.core.exceptions import ValidationError
from accounts.utils.import_utils import import_accounts, FileTypeNotSupported
from accounts.models import Account
import io
import csv
import json

class ImportUtilsTestCase(TestCase):
    def setUp(self):
        # Setup code before each test (e.g., creating initial test data)
        self.sample_csv = io.StringIO("ID,Name,Balance\n1,John Doe,1000\n2,Jane Doe,2000")
        self.sample_json = '[{"ID": "1", "Name": "John Doe", "Balance": 1000}, {"ID": "2", "Name": "Jane Doe", "Balance": 2000}]'


    def test_import_json(self):
        # Testing import from JSON
        import_accounts(io.StringIO(self.sample_json), file_type='json')
        
        # Check if the accounts were created
        self.assertEqual(Account.objects.count(), 2)
        jane_doe = Account.objects.get(account_number="2")
        self.assertEqual(jane_doe.account_holder_name, "Jane Doe")
        self.assertEqual(jane_doe.balance, 2000)

    def test_invalid_file_type(self):
        # Testing for unsupported file type
        with self.assertRaises(FileTypeNotSupported):
            import_accounts(io.StringIO("Invalid Data"), file_type="xml")
