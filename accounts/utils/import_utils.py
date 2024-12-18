import csv
import json
import pandas as pd  
from accounts.models import Account

class FileTypeNotSupported(Exception):
    pass

def import_accounts(file, file_type="csv"):
    """
    Import accounts from a generic file.
    Args:
        file: The uploaded file object
        file_type: Type of file ("csv", "json", "excel")
    Raises:
        FileTypeNotSupported: If the file type isn't supported.
    """
    if file_type == "csv":
        data = csv.DictReader(file.read().decode("utf-8").splitlines())
    elif file_type == "json":
        data = json.loads(file.read())
    elif file_type in ["excel", "xlsx"]:
        data = pd.read_excel(file, sheet_name=0).to_dict(orient="records")
    else:
        raise FileTypeNotSupported(f"{file_type} is not supported.")

    # Process the data
    for row in data:
        account, created = Account.objects.get_or_create(
            account_number=row["ID"],
            defaults={
                "account_holder_name": row["Name"],
                "balance": row["Balance"],
            }
        )
        if not created:
            # Optionally update the record
            account.account_holder_name = row["Name"]
            account.balance = row["Balance"]
            account.save()
