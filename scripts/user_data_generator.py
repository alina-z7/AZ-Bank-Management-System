import os
import random
from faker import Faker

fake = Faker()

user_data = []
for u in range(75):
    username = f"user{u+1}"
    password = fake.password(length=10)
    user_data.append(f"User,{username},{password}")

customer_data = []
for c in range(50):
    user_id = c + 1
    phone_num = fake.phone_number()
    address = fake.address().replace("\n", ", ")
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%Y-%m-%d")
    customer_data.append(f"Customer,{user_id},{phone_num},{address},{date_of_birth}")

employee_data = []
for e in range(25):
    user_id = e + 51
    phone_num = fake.phone_number()
    address = fake.address().replace("\n", ", ")
    position = random.choice(["Manager", "Analyst", "Assistant", "Consultant"])
    employee_data.append(f"Employee, {user_id},{phone_num},{address},{position}")

output_file_path = os.path.join("data", "UserData.txt")

with open(output_file_path, "w") as file:
    file.write("# User data\n")
    file.write("User,username,password\n")
    file.write("\n".join(user_data))
    file.write("\n\n# Customer data\n")
    file.write("Customer,user_id,phone_number,address,date_of_birth\n")
    file.write("\n".join(customer_data))
    file.write("\n\n# Employee data\n")
    file.write("Employee,user_id,phone_number,address,position,hire_date\n")
    file.write("\n".join(employee_data))