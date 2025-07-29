Library Management System - RESTful API
This repository contains a RESTful API for a Library Management System, built with Django and Django REST Framework. The API manages book records, user registrations, and borrowing history, providing a complete backend solution for a library application.

Features
User Authentication: Secure user registration and JWT-based authentication (login/logout).

Book Management (CRUD):

Add new books to the library.

View a list of all books or retrieve a single book by its ID.

Update book details.

Delete books from the system.

Borrowing System:

Authenticated users can borrow available books.

Authenticated users can return books they have borrowed.

A book's availability is automatically updated when it is borrowed or returned.

Borrowing History: Users can view their personal history of borrowed books.

API Documentation: Interactive API documentation powered by Swagger (drf-yasg) is available to easily test and explore all endpoints.

Database: Uses MySQL for robust and scalable data storage.

Setup and Installation
To get this project up and running on your local machine, please follow these steps.

Prerequisites
Python (3.8 or higher)

Git

MySQL Server

1. Clone the Repository
git clone <repository-url>
cd <repository-name>

2. Create and Activate a Virtual Environment
It is highly recommended to use a virtual environment to manage project dependencies.

# Create the virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies
The required Python packages are listed in the requirements.txt file.

pip install -r requirements.txt

4. Set Up the Database
Make sure your MySQL server is running.

Log in to your MySQL client and create a new database:

CREATE DATABASE library_db;

In the project, navigate to library_project/settings.py and update the DATABASES configuration with your MySQL credentials (username, password, port).

5. Run Database Migrations
This will create all the necessary tables in your database.

python manage.py migrate

6. Create a Superuser
This creates an admin account for the Django admin interface.

python manage.py createsuperuser

7. Run the Development Server
python manage.py runserver

The API will now be running at http://127.0.0.1:8000/.

API Usage and Endpoints
You can explore and test all the API endpoints through the interactive Swagger documentation.

API Documentation URL: http://127.0.0.1:8000/api/docs/

Main Endpoints
/api/register/ - POST: Create a new user.

/api/token/ - POST: Log in to get an access and refresh token.

/api/token/refresh/ - POST: Get a new access token using a refresh token.

/api/books/ - GET, POST: List all books or create a new book.

/api/books/{id}/ - GET, PUT, PATCH, DELETE: Retrieve, update, or delete a specific book.

/api/books/{id}/borrow/ - POST: Borrow a book.

/api/books/{id}/return_book/ - POST: Return a borrowed book.

/api/history/ - GET: View your personal borrowing history.

To access protected endpoints, you must first obtain a token from /api/token/ and authorize your requests by including it in the Authorization header as a Bearer token.