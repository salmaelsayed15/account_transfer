from django.urls import path
from .views import account_list, account_detail, transfer_funds,import_accounts_view

urlpatterns = [
    path('accounts/', account_list, name='account-list'),
    path('accounts/<str:account_number>/', account_detail, name='account-detail'), 
    path('transfer/', transfer_funds, name='transfer-funds'),
    path('import/', import_accounts_view, name='import-accounts'),

]
