# AZ Bank Management System

This is a comprehensive bank management system developed using Django for the backend and React for the frontend.

## Features

- **User Management**: Manages customers and employees.
- **Account Management**: Handles various account-related functionalities.
- **Transactions**: Records and manages transactions.
- **Loan and Card Management**: Handles loan and card functionalities.
- **Employee Management**: Manages employee-related data.

## Tech Stack

- **Backend**: Python 3, Django, Django REST framework
- **Frontend**: React, JavaScript, HTML5, CSS3
- **Database**: MySQL 
- **APIs**: Django REST framework

## Installation

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
