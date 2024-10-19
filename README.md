# Django Noviindus Assessment 

## Introduction

This is a **Product Management Tool** built with Django. It allows users to view products, add products to a shopping cart, edit and delete products, and manage orders. The project follows MVT architecture and uses Django's built-in functionality to manage forms, handle media files, and more.

## Features
- User Authentication(Registrations and Login )
- List all products with their details.
- Add products to a cart.
- Edit or delete existing products.
- Manage product images and descriptions.
- View total price and quantity in the cart.

  
## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite (can be changed to PostgreSQL or MySQL)


## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Virtualenv
- Git

### Steps
1. **Clone the repository:**
    ```bash
    git clone https://github.com/mathew-star/Noviindus_assesment.git
    cd Assessment
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    Apply migrations to set up the initial database schema:
    ```bash
    python manage.py migrate
    ```



5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

Now you can visit `http://127.0.0.1:8000/` in your browser.


