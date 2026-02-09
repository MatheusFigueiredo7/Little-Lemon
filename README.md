# Little Lemon API - Capstone Project 🍋

## The Chosen Project 🎯

This project is a robust API developed as part of the **Capstone Project** for the **Meta Back-End Developer Professional Certificate**. The goal was to create a complete backend system for the fictional restaurant "Little Lemon," allowing customers to browse the menu and book tables, while managers and admins have full control over inventory and operations.

The application was built using **Django** and **Django REST Framework (DRF)**, focusing on API design best practices, security, authentication, and performance.

## Implemented Features ⚙️

The developed system includes the following main features:

* **Menu Management (Menu API)**: Complete CRUD endpoints to list, create, update, and delete menu items.
* **Booking System**: Allows authenticated users to book tables for specific dates and times.
* **Robust Authentication**: Implementation of Token-based and Session authentication using the **Djoser** library.
* **Access Control (Permissions)**:
    * **Customers**: Can view the menu and make bookings.
    * **Managers**: Can manage menu items and delivery crew.
    * **Admins**: Full access to the system.
* **Filtering, Ordering, and Pagination**: Advanced features to facilitate searching for menu items by price, category, etc.
* **Throttling (Rate Limiting)**: API protection against request overload, ensuring stability.
* **Automated Testing**: Unit tests to guarantee the integrity of endpoints and business rules.

## Technologies Used 🛠️

* **Python**: Main language of the project.
* **Django**: High-level web framework for rapid development.
* **Django REST Framework (DRF)**: Powerful toolkit for building Web APIs.
* **Djoser**: Library for authentication and user management.
* **Pipenv**: Dependency management and virtual environment.
* **SQLite/MySQL**: Database for information persistence.
* **Insomnia / Postman**: Tools used to test API requests.

## Project Structure 📁

```bash
Little-Lemon/
├── littlelemon/            # Main project settings (Settings, Base URLs)
├── restaurant/             # Main app containing business logic
│   ├── migrations/         # Database migration files
│   ├── models.py           # Data models (Menu, Booking, etc.)
│   ├── serializers.py      # Serializers for data conversion
│   ├── urls.py             # API-specific routes
│   └── views.py            # Controllers (ViewSets and Generics)
├── media/                  # Media files (dish images)
├── manage.py               # Django command-line utility
├── Pipfile                 # Dependency definition file
├── Pipfile.lock            # Version lock file
├── db.sqlite3              # Local database (default)
└── README.md               # This file

```

## Main API Endpoints 🔗

Here are some of the routes available for testing:

| Method | Endpoint | Description | Permission |
| --- | --- | --- | --- |
| `GET` | `/api/menu-items/` | Lists all dishes | Anyone |
| `POST` | `/api/menu-items/` | Adds a new dish | Manager/Admin |
| `GET` | `/api/bookings/` | Lists bookings | Authenticated User |
| `POST` | `/api/token/login/` | Generates access token | Anyone |
| `POST` | `/api/users/` | Creates a new user | Anyone |

## How to Run the Project 🚀

To run the API locally, follow the steps below:

### 1. Clone the Repository 🧑‍💻

Clone the repository using the Git command:

```bash
git clone [https://github.com/MatheusFigueiredo7/Little-Lemon.git](https://github.com/MatheusFigueiredo7/Little-Lemon.git)

```

### 2. Navigate to the Directory 📂

```bash
cd Little-Lemon

```

### 3. Install Dependencies 📦

Ensure you have `pipenv` installed and run:

```bash
pipenv install
pipenv shell

```

### 4. Configure the Database 🗄️

Apply migrations to create the necessary tables:

```bash
python manage.py migrate

```

### 5. Run the Server 🌐

Start the development server:

```bash
python manage.py runserver

```

The API will be available at `http://127.0.0.1:8000/`.

## Testing the API 🧪

To test the endpoints:

1. Access `http://127.0.0.1:8000/api/menu-items/` in your browser or via Insomnia/Postman.
2. For administrative features, create a superuser:
```bash
python manage.py createsuperuser

```


3. Login to the admin panel at `http://127.0.0.1:8000/admin/`.

---
