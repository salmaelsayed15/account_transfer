import csv
from django.core.management.base import BaseCommand
from accounts.models import Account

class Command(BaseCommand):
    help = "Import accounts from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        try:
            with open(csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    account, created = Account.objects.get_or_create(
                        account_number=row['ID'],  # Update to match your CSV
                        defaults={
                            'account_holder_name': row['Name'],  # Update to match your CSV
                            'balance': row['Balance']  # Update to match your CSV
                        }
                    )
                    if created:
                        self.stdout.write(f"Imported {account}")
                    else:
                        self.stdout.write(f"Skipped {account}, already exists")
        except Exception as e:
            self.stderr.write(f"Error: {str(e)}")
