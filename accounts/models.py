from django.db import models

# Create your models here.
from django.db import models

class Account(models.Model):
    account_number = models.CharField(max_length=20, unique=True)
    account_holder_name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.account_holder_name} - {self.account_number}"
