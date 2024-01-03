from rest_framework import serializers
from .models import User, Customer, Employee, Account, Card, Loan, Transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()  
    class Meta:
        model = Customer
        fields = ('id', 'user', 'phone_number', 'address', 'date_of_birth')

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer() 
    class Meta:
        model = Employee
        fields = ('id', 'user', 'phone_number', 'address', 'position', 'hire_date')

class AccountSerializer(serializers.ModelSerializer):
    branch = serializers.PrimaryKeyRelatedField(read_only=True)
    employee = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Account
        fields = ('id', 'account_number', 'balance', 'account_type', 'is_active', 'open_date', 'close_date', 'branch', 'employee')

class CardSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Card
        fields = ('id', 'card_number', 'card_type', 'is_active', 'issue_date', 'expiry_date', 'account')

class LoanSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Loan
        fields = ('id', 'loan_amount', 'interest_rate', 'start_date', 'end_date', 'is_approved', 'account')

class TransactionSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Transaction
        fields = ('id', 'amount', 'transaction_type', 'date_time', 'description', 'account')
