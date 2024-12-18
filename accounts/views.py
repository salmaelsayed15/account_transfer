from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse 
from .models import Account
from django.contrib import messages 
from django.core.exceptions import ValidationError
from decimal import Decimal 
import csv
from io import StringIO
from accounts.utils.import_utils import import_accounts, FileTypeNotSupported

# Account List view
def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'accounts/account_list.html', {'accounts': accounts})

# Account Detail view
def account_detail(request, account_number):
    # Retrieve account using the account_number passed in the URL
    account = get_object_or_404(Account, account_number=account_number)
    return render(request, 'accounts/account_detail.html', {'account': account})


def transfer_funds(request):
    if request.method == "POST":
        # Get POST data (form inputs)
        from_account_number = request.POST['from_account']
        to_account_number = request.POST['to_account']
        transfer_amount = Decimal(request.POST['amount'])  # Convert the amount to a Decimal 

        # Get the account instances using account numbers
        from_account = Account.objects.get(account_number=from_account_number)
        to_account = Account.objects.get(account_number=to_account_number)

        # Check if the 'from' account has enough balance
        if from_account.balance >= transfer_amount:
            # Proceed with the transfer
            from_account.balance -= transfer_amount  # Subtract from sender's account
            to_account.balance += transfer_amount  # Add to receiver's account

            from_account.save()  # Save the changes
            to_account.save()  # Save the changes

            messages.success(request, f"Successfully transferred ${transfer_amount} from {from_account.account_holder_name} to {to_account.account_holder_name}.")
            print(f"Message: {'Successfully transferred'}")

            # Redirect to account list or show success message
            return redirect('account-list')  # Redirects to the account list page
        else:
            # If insufficient funds
            messages.error(request, f"Error! Insufficient funds for this transfer.\n Trying to transfer {transfer_amount} while the current balance is {from_account.balance}")
            print(f"Message: {'Error transferring funds!'}")
            return redirect('transfer-funds')  # Optionally, redirect back to the transfer page

    return render(request, 'accounts/transfer_form.html')  # Display form if not POST request


def import_accounts_view(request):
    if request.method == "POST":
        file = request.FILES.get("file")
        file_type = request.POST.get("file_type", "csv").lower()
        Account.objects.all().delete()  # Deletes all existing Account records

        try:
            import_accounts(file, file_type=file_type)
            messages.success(request, "Accounts imported successfully!")
        except FileTypeNotSupported as e:
            messages.error(request, f"File type {file_type} is not supported.")
            return render(request, "accounts/import_accounts.html", {"error": str(e)})  # Render same page with error message
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return render(request, "accounts/import_accounts.html", {"error": str(e)})

        return redirect("account-list")
    return render(request, "accounts/import_accounts.html")