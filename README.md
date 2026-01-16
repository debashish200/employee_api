# Employee Management REST API (Django)

## 📌 Project Overview

This project is a **secure RESTful API** built using **Django and Django REST Framework** to manage employees in a company.  
It supports **CRUD operations**, **JWT-based authentication**, **pagination**, **filtering**, **validation**, and **unit testing**.

The project is developed as part of the **HabotConnect – Python Backend Developer Hiring Assignment**.

---

## 🚀 Features

- JWT Authentication (Access & Refresh Tokens)
- Create, Read, Update, Delete (CRUD) Employees
- Secure endpoints (authentication required)
- Pagination (10 employees per page)
- Filtering by department and role
- Proper HTTP status codes and error handling
- Unit tests for key scenarios

---

## 🛠 Tech Stack

- Python 3.x
- Django
- Django REST Framework
- Simple JWT
- SQLite (default database)

---

## 📂 Project Structure

employee_api/
│
├── employee_api/
│ ├── settings.py
│ ├── urls.py
│ └── asgi.py
│
├── employees/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ ├── tests.py
│ └── migrations/
│
├── manage.py
