A simple blog application using Django 4.2.3 and Python 3.11.4. The application is run on a local server and uses PostgreSQL as the database.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt 
```
## Usage

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

## Features

- Add/Delete Posts
- Add/Delete Comments
- Add Tags to Posts
- Search Posts by Tags
- Search Posts by Title
- Search Posts by Author
- Recommended Posts
- Pagination

## Technologies

- Django 4.2.3
- Python 3.11.4
- PostgreSQL
- HTML
- CSS
- Bootstrap 5