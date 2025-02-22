
---

# Articlesdb API

This is a Django REST framework-based API for managing articles, comments, and tags. Follow the instructions below to set up the project, add sample data, and run the API.

---

## Table of Contents

1. [Project Setup](#project-setup)
2. [Adding Sample Data](#adding-sample-data)
3. [Running the API](#running-the-api)

---

## Project Setup

### Prerequisites

1. **Python 3.x** installed on your system.
3. **Virtualenv** (optional).

### Steps to Set Up the Project

1. Clone the repository:

    ```
    git clone <github_repo>
    cd articlesDB
    ```

2. Create and activate a Python virtual environment:

    ```
    python -m venv venv
    source venv/bin/activate  
    # For Windows use: venv\Scripts\activate
    ```

3. Install the dependencies:

    ```
    pip install -r requirements.txt
    ```


## Adding Sample Data

### Using Django Fixtures

You can load predefined sample data using Django fixtures. 

**Importart**: the fixtures must be inserted in order

### Prerequisite: 
In order for the fixtures (which are static data) to work correctly, you must have 3 users already created and given the superuser and staff status. 
The first user is created through the ```python manage.py createsuperuser``` command. 
The others can be created in the admin panel. 

#### Remove and reset the sqlite:

    
    rm db.sqlite3

**Note**: If something is not working try to remove, also, the migration files. 
    

#### To migrate the data to the database run the command:

    
    python manage.py makemigrations
    python manage.py migrate
    

#### Create a superuser:

    
    python manage.py createsuperuser
    
After creating the superuser, login at:
    ```
    http://127.0.0.1:8000/admin/login/?next=/admin/login``` to be able to perform actions to the api.
    Create a user in order to be authenticated.

### Note:
    In order for the Django fixtures to work correctly, you must have users already created.. The first is already created through the ```python manage.py createsuperuser``` command. The others can be created in the admin panel.
    

#### load the tags data using the command:

    
    python manage.py loaddata tags.json  


#### load the authors data using the command:

    
    python manage.py loaddata authors.json  
    

#### insert the articles data running this command:

    
    python manage.py loaddata articles.json  
    

#### add the comments data with the command:

    
    python manage.py loaddata comments.json  

**Note**: Additional way to add data:
        1. Via Django Admin Panel (connect with admin credentials)
        2. Via Django shell




## Running the API

### Steps to Start the API Server

1. Start the development server using the command:

    ```
    python manage.py runserver
    ```

2. Login to perform actions for the api(add users, change data)
    
    ```
    http://127.0.0.1:8000/admin/auth/user/
    ```

3. The API will be available at `http://127.0.0.1:8000/`.

4. The following endpoints are available:
   - `/api/articles/` – View, create, and manage articles.
   - `/api/tags/` – Manage tags.
   - `/api/comments/` – Manage comments.
   - `/api/articles/export_csv/` – Export articles as a CSV file.

---

    Example for article POST method:
    ```
    {
    "identifier": "a111",
    "publication_date": "2023-10-02",
    "authors": [{"name": "Alice Johnson"}],
    "abstract": "test",
    "title": "test",
    "tags":[{"name": "wwww"}]
    }
    ```
