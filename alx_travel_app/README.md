# 🧳 ALX Travel App (alx_travel_app_0x00)

A backend application for a travel booking platform built with **Django** and **Django REST Framework (DRF)**. This project provides a RESTful API to manage travel listings, user bookings, and reviews. It serves as a practical example of building a scalable, API-driven web service.

---

## ✨ Key Features

-   **Listings Management**: CRUD (Create, Read, Update, Delete) operations for travel listings.
-   **Booking System**: Endpoints for users to create and manage their bookings.
-   **User Reviews**: Functionality for users to leave reviews and ratings on listings.
-   **Database Seeding**: A custom management command to populate the database with sample data for easy testing.
-   **Environment-Based Configuration**: Securely manages settings like secret keys and database credentials using a `.env` file.

---

## 🚀 Tech Stack

-   **Backend**: Python, Django
-   **API**: Django REST Framework (DRF)
-   **Database**: SQLite (default for development)
-   **Environment Variables**: `django-environ`
-   **Data Seeding**: `Faker` library for generating sample data

---


### Run Database Migrations

**Apply the database schema changes.**

    python manage.py makemigrations
    python manage.py migrate

---
### API Endpoints

The core API endpoints available are:

| Method | Endpoint              | Description                      |
| :----- | :-------------------- | :------------------------------- |
| `GET`  | `/api/listings/`      | Retrieve a list of all listings. |
| `POST` | `/api/listings/`      | Create a new listing.            |
| `GET`  | `/api/listings/<id>/` | Retrieve a single listing.       |
| `POST` | `/api/bookings/`      | Create a new booking.            |

*(Note: Add more endpoints here as the project grows, such as for reviews or user authentication.)*
