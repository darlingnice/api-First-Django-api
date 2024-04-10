python
Copy code
# Django API Trial App

This is a simple Django application created as a trial for building APIs using Django REST Framework.

## Description

This project serves as a basic demonstration of creating RESTful APIs with Django. It includes a simple API for managing users, posts, or any other relevant entities.

## Requirements

- Python (>=3.6)
- Django (>=3.0)
- Django REST Framework (>=3.11)

## Installation

1. Clone the repository:
git clone https://github.com/darlingnice/api-First-Django-api.git
cd api-First-Django-api
2. Create a virtual environment (optional but recommended):
   python -m venv venv  # On Windows
   python3 -m venv venv  # On Unix/Mac
   
source venv/bin/activate # On Unix/Mac
venv\Scripts\activate.bat # On Windows


3. Install the dependencies:
pip install -r requirements.txt

4. Apply migrations:
5. Run the development server:
   python manage.py runserver # On Windows
   python3 manage.py runserver # On Unix/Mac


6. Access the API in your web browser or using tools like Postman:
http://localhost:8000/api/v1/getData/ # for GET request .to get the api data returned
http://localhost:8000/api/v1/addData/  #for POST request . to add new data

   

