# Rivyou Product Search API

A Django REST Framework backend application with JWT Authentication and Product Search functionality using PostgreSQL.

## Features

* User Registration
* JWT Authentication
* Product Search API
* PostgreSQL Database
* CSV Product Import
* Protected Endpoints
* Relevance Based Search

## Tech Stack

* Python 3.10
* Django 5
* Django REST Framework
* PostgreSQL 16
* Simple JWT
* Pandas

## Installation

Clone repository:

```bash
git clone <repository_url>
cd rivyou_backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Import products:

```bash
python manage.py import_products
```

Run server:

```bash
python manage.py runserver
```

## API Endpoints

### Register

POST

```text
/api/auth/register/
```

### Login

POST

```text
/api/auth/login/
```

### Product Search

GET

```text
/api/products/search/?q=smartphone
```

Authorization:

```text
Bearer <access_token>
```

## Database

PostgreSQL

Database Name:

```text
rivyou_db
```

## Sample Search

```text
/api/products/search/?q=headphones
```

## Author

MohammedJakeer F Maniyar
