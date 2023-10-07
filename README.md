# Fred's Portfolio Backend

Welcome to the backend repository of my personal portfolio! This section powers the dynamic content on the frontend, built using Django and the Django Rest Framework.

## Features

- **RESTful API**: Provides endpoints for fetching projects, blogs, and other portfolio content.
- **Database Integration**: Efficiently fetches and stores data using Django's ORM.
- **Admin Dashboard**: Utilizing Django's built-in admin interface for content management.

## Technologies Used

- Framework: Django, Django Rest Framework
- Database: (Your choice, e.g., PostgreSQL, SQLite)

## Local Setup

1. Clone the backend repository:
```bash
   git clone https://github.com/yourusername/portfolio-backend.git
```
2. Navigate to the project directory:
```
cd portfolio-backend
```
3. Set up a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
4. Install the required dependencies:
```
pip install -r requirements.txt
```
5. Run migrations:
```
python manage.py migrate
```
6. Start the development server:
```
python manage.py runserver
```

The API should now be running on http://localhost:8000.
