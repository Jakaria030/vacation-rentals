# Vacation Rentals
A Django-based web application for browsing and searching vacation rental properties by location, complete with property details, images, and pagination.  


## 🚀 Features
- Browse vacation rentals by location, city, or country.  
- Property cards with title, price per night, facilities, likes, reviews, and images.  
- Pagination with 20 properties per page.  
- Search functionality with suggestions (autocomplete).  
- Import property and location data from CSV.  

## 🛠 Tech Stack
- **Backend:** Django (Python)
- **Database:** SQLITE3
- **Templating:** Django Tags


## 📂 Project Structure
```bash
vacation-rentals/
├── media/
│   └── image.jpg
├── properties/
│   ├── data/
│   │   └── properties.csv
│   ├── management/
│   │   └── commands/
│   │       └── import_properties.py
│   ├── migrations/
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   └── index.html
│   │   └── master.html
│   │   └── properties.html
│   │   └── properties_details.html
│   ├── templatetags/
│   │   └── custom_filters.py
│   ├── admin.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── vacation_rentals/
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt

```

## Getting Started
Follow these steps to set up and run the project locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/Jakaria030/vacation-rentals.git
    ```
2. Navigate to the project directory:
    ```bash
    cd vacation-rentals
    ```
3. Create Virtual Environment
    ```bash
    python3 -m venv .venv # for linux
        
    python -m venv .venv # for windows
    ```
4. Activate Virtual Environment
    ```bash
    source .vevn/bin/activate # for linux
    vevn\Scripts\activate # for windows
    ```
5. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```
6. Save Intsalled Packages (optional)
    ```bash
    pip freeze > requirements.txt
    ```
7. Apply migrations
    ```bash
    python manage.py migrate
    ```
8. Load sample data (optional)
    ```bash
    python manage.py import_properties
    ```
    This command reads the CSV file properties/data/properties.csv and loads all locations and properties into the database.
9. Run the development server
    ```bash
    python manage.py runserver
    ```

📝 Notes

- The SQLite database (db.sqlite3) is not included in the repository. Each developer must create their own by running migrations.
- To upload property images, you must create a superuser and upload images manually through the Django admin.
- All properties already have a default image so the site looks correct before uploading real images.

1. Create a superuser
    ```bash
    python manage.py createsuperuser
    ```
    - You will be prompted to enter:
    - Username
    - Email (optional)
    - Password

    Once created, login to the admin panel at: http://127.0.0.1:8000/admin/ and upload images


## Additional Resources
- [Django Documentation](https://docs.djangoproject.com/en/6.0/topics/)
