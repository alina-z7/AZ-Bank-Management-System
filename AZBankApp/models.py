from django.db import models

class User(models.Model):
    username = models.CharField(max_length=8)
    password = models.CharField(max_length=12)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=25)
    date_of_birth = models.DateField()

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=25)
    position = models.CharField(max_length=25)
    hire_date = models.DateField()

class Account(models.Model):
    account_number = models.CharField(max_length=10)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    account_type = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    open_date = models.DateTimeField()
    close_date = models.DateTimeField(null=True, blank=True)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Card(models.Model):
    card_number = models.CharField(max_length=16)
    card_type = models.CharField(max_length=7)
    is_active = models.BooleanField(default=True)
    issue_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

class Loan(models.Model):
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_approved = models.BooleanField(default=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    description = models.CharField(max_length=255)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
