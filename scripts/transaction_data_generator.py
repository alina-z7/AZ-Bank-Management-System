from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

transactions = []
for _ in range(100):  
    amount = round(random.uniform(10, 1000), 2) 
    transaction_type = random.choice(['Deposit', 'Withdrawal', 'Transfer'])
    date_time = fake.date_time_between(start_date='-1y', end_date='now')
    description = fake.sentence()
    
    transactions.append({
        'amount': amount,
        'transaction_type': transaction_type,
        'date_time': date_time,
        'description': description,
    })

output_filename = 'fake_transactions.txt'
with open(output_filename, 'w') as file:
    for transaction in transactions:
        file.write(f"{transaction}\n")
