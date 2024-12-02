# FastAPI CRUD Operations

FastAPI CRUD Operations is a Python web application built using **FastAPI**, **SQLAlchemy**, and **JWT authentication**. This project demonstrates how to handle user registration, login, and manage item data with CRUD operations. The app allows users to register, log in to get an authentication token, and perform create, read, update, and delete operations on items.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
  - [Authentication](#authentication)
  - [CRUD Operations](#crud-operations)
- [Testing](#testing)
- [Contributing](#contributing)
- [Documentation](#documentation)

## Features

- **User Authentication**: Register and login users with JWT token-based authentication.
- **CRUD Operations for Items**: Create, read, update, and delete items.
- **User Profile**: Access the user's profile based on the JWT token.
- **Data Validation**: Ensures data integrity with user registration and item management.

## Installation

To install and run the FastAPI CRUD Operations project, follow the steps below:

### Installation via `pip` (Recommended)

To install the required dependencies, you can run:

```bash
pip install -r requirements.txt
```

This will install all the necessary dependencies, including FastAPI, SQLAlchemy, Pydantic, passlib, and python-jose.

### Optional: Create a virtual environment

To avoid conflicts with other Python packages, it's recommended to create a virtual environment:

1. Create a virtual environment:

```bash
python -m venv venv
```

2. Active the virtual environment:

    * On Windows:

    ```bash
    venv\Scripts\activate
    ```

    * On macOS/Linux

    ```bash
    source venv/bin/activate
    ```

3. Install the project dependencies:

```bash
pip install -r requirements.txt
```

### Run the Application

To run the FastApi application, use:

```bash
uvicorn app.main:app --reload
```

This will start the server on http://localhost:8000

## Usage

To use the FastAPI CRUD Operations, follow the steps below:

1. Register a new user: Send a POST request to /register to     create a new user.

2. Login the user: Send a POST request to /login to get a JWT token for authentication.

3. Perform CRUD operations on items: Once logged in, use the token to create, read, update, and delete items.

### Example Usage

#### Register User

```bash
POST /register
```

#### Request Body

```bash
{
  "username": "newuser",
  "password": "newpassword"
}
```

#### Response

```bash
{
  "id": 1,
  "username": "newuser"
}
```

#### Login

```bash
POST /login
```

#### Request Body

```bash
{
  "username": "newuser",
  "password": "newpassword"
}
```

#### Response

```bash
{
  "access_token": "your_jwt_token_here",
  "token_type": "bearer"
}
```

#### Get Items

```bash
GET /item
```

#### Response

You will see the full list of items in the following format.
```bash
[
  {
    "id": 1,
    "name": "New Item",
    "description": "This is a new item.",
    "price": 100.50,
    "category": "Electronics",
    "brand": "BrandX"
  }
]
```

#### Specific Item

```bash
GET /item/{item_id}
```
#### Sorting and Filtering

```bash
GET /items?search="your_input"&sort="your_input"
```

#### Add Item

```bash
POST /item
```

#### Request Body

```bash
{
  "name": "New Item",
  "description": "This is a new item.",
  "price": 100.50,
  "category": "Electronics",
  "brand": "BrandX"
}
```

#### Response

```bash
{
  "id": 1,
  "name": "New Item",
  "description": "This is a new item.",
  "price": 100.50,
  "category": "Electronics",
  "brand": "BrandX"
}
```
#### Update Item

```bash
PUT /items/{item_id}
```

#### Request Body

```bash
{
  "name": "Updated Item",
  "description": "This is an updated item.",
  "price": 150.00,
  "category": "Home Appliances",
  "brand": "BrandY"
}
```

#### Response

```bash
{
  "id": 1,
  "name": "Updated Item",
  "description": "This is an updated item.",
  "price": 150.00,
  "category": "Home Appliances",
  "brand": "BrandY"
}
```

#### Detete Item

```bash
DELETE /item/{item_id}
```

#### Response

```bash
{
  "detail": "Item deleted successfully"
}
```

## Modules

### Authentication

The **authentication module** handles user registration, login, and JWT token management.

- **Register User**: Registers a new user with a username and password.
- **Login User**: Authenticates a user and returns a JWT token for future requests.
- **Get Current User**: Retrieves the current authenticated user based on the JWT token.

### CRUD Operations

The **CRUD operations module** enables the management of item data. It includes functions to create, read, update, and delete items in the database.

- **Create Item**: Creates a new item by providing details such as `name`, `description`, `price`, `category`, and `brand`.
- **Read Item(s)**: Fetches a list of items or a specific item by ID.
- **Update Item**: Modifies an existing item by updating its details.
- **Delete Item**: Deletes an item from the database.

## Testing

To test the FastAPI CRUD Operations project, you can use **Postman** or any API testing tool. Here are the steps:

1. **Register a new user** by sending a POST request to `/register`.
2. **Login the user** and get the JWT token from the `/login` endpoint.
3. **Create, read, update, and delete items** using the token as authorization in the headers (`Authorization: Bearer <token>`).

Alternatively, you can write unit tests using **pytest** and the `TestClient` from FastAPI:

```bash
pytest
```

### Test Structure

Tests are located in the **tests/** directory, with individual test files for each module (e.g., **test_auth.py**, **test_items.py**). The tests verify the core functionality, edge cases, and correctness of the methods.

## Contributing

We welcome contributions to FastAPI CRUD Operations! If you'd like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to your forked repository (`git push origin feature-branch`).
5. Open a pull request.

Please ensure your code adheres to the existing code style and includes tests where appropriate.

## Documentation

For more detailed documentation on the technologies used in this project, refer to the following resources:

- [FastAPI Documentation](https://fastapi.tiangolo.com/): FastAPI's official documentation.
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/): Official documentation for SQLAlchemy ORM.
- [JWT Documentation (python-jose)](https://pyjwt.readthedocs.io/en/latest/): Documentation for the JWT token handling used in this project.
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/): Official documentation for Pydantic, used for data validation and models.
