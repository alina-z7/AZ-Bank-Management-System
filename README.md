# AZ Bank Management System

This is a comprehensive bank management system developed using Django for the backend and React for the frontend.

## Features

- **User Management**: Manages customers and employees.
- **Account Management**: Handles various account-related functionalities.
- **Transactions**: Records and manages transactions.
- **Loan and Card Management**: Handles loan and card functionalities.
- **Employee Management**: Manages employee-related data.

## Tech Stack

- **Backend**: Python 3, Django
- **Frontend**: React, JavaScript, Bootstrap, HTML5, CSS3, Tailwind CSS
- **Database**: MySQL 
- **APIs**: Faker, Django REST framework

### Faker for Placeholder Data

The Faker library is used to generate realistic placeholder data for testing and development purposes. This helps simulate real-world scenarios and aids in the development and testing of your bank management system.

In the `scripts/` directory, you can find scripts that utilize Faker to generate sample data. These scripts can be run to populate your database with test data, making it easier to evaluate and fine-tune your application.

To use Faker for generating data, follow these steps:

1. Navigate to the `scripts/` directory.
2. Run the relevant script for the data you want to generate. For example, `python generate_customer_data.py` for creating sample customer data.
3. Check your Django admin panel or API endpoints to see the newly generated data.

Note: Remember to use this data responsibly and only for development and testing purposes.

### Backend (Django)

1. Clone this repository.
2. Navigate to the `backend` directory.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run migrations: `python manage.py migrate`.
5. Start the backend server: `python manage.py runserver`.

### Frontend (React)

1. Navigate to the `frontend` directory.
2. Install dependencies: `npm install`.
3. Start the frontend server: `npm start`.

## Usage

1. Register customers and employees via the Django admin panel or APIs.
2. Access different functionalities through the provided UI in the frontend.
3. Utilize the API endpoints for integration or custom use cases.

## File Structure

- **AZBankApp/**: Django backend code.
- **frontend/**: React frontend code.
- **scripts/**: Project data generators.
- **data/**: Placeholder data for development.

## License

This project is licensed under the [MIT License](LICENSE).
