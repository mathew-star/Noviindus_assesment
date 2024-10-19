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
    To package up your model changes into individual migration files:
    ```bash
    python manage.py makemigrations
    ```

5. **Set up the database:**
    Apply migrations to the database:
    ```bash
    python manage.py migrate
    ```



6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

Now you can visit `http://127.0.0.1:8000/` in your browser.


![Assesment Homepage](https://github.com/user-attachments/assets/6c814373-6b1c-41c7-adda-c125b73ad007)

![Assesment Product page](https://github.com/user-attachments/assets/0986358e-febd-441b-9cd8-3d434af45c8a)

![Assesment add product](https://github.com/user-attachments/assets/0325f596-c16c-4bcd-908a-02e41e47f96a)

![Assesment edit product](https://github.com/user-attachments/assets/d85fb3ea-4c1e-4e3c-845a-7e74e75a1836)

![Assesment cart](https://github.com/user-attachments/assets/fc375e7c-6c76-4ef0-b9ca-4a6c62aa449d)

![Assesment removing product from cart](https://github.com/user-attachments/assets/4e6df96d-ccf6-4fa3-b43c-f1744d97dc41)


