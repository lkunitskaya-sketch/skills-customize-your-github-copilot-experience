# 📘 Assignment: Building a CRUD API with SQLAlchemy

## 🎯 Objective

Learn how to build a persistent REST API by connecting FastAPI endpoints to a SQLite database using SQLAlchemy ORM. You'll implement complete CRUD (Create, Read, Update, Delete) operations for a data model.

## 📝 Tasks

### 🛠️ Set Up SQLAlchemy and Create a Database Model

#### Description
Configure SQLAlchemy to work with a SQLite database and define a database model for storing book information.

#### Requirements
Completed program should:

- Import and configure SQLAlchemy with a SQLite database (e.g., `books.db`)
- Define a `Book` model with at least `id` (primary key), `title` (string), `author` (string), and `year` (integer) fields
- Create the database table when the app starts (using `Base.metadata.create_all()`)
- Include a Pydantic model (`BookCreate`) for request validation

### 🛠️ Implement the POST Endpoint to Create Books

#### Description
Add a `POST /books` endpoint that accepts book data, saves it to the database, and returns the created book record.

#### Requirements
Completed program should:

- Accept a JSON request body matching the `BookCreate` model
- Save the book to the database and flush/commit the session
- Return the created book with its assigned `id` from the database
- Handle database errors gracefully

Example request:
```json
{ "title": "1984", "author": "George Orwell", "year": 1949 }
```

Example response:
```json
{ "id": 1, "title": "1984", "author": "George Orwell", "year": 1949 }
```

### 🛠️ Implement the GET Endpoint to Retrieve Books

#### Description
Add a `GET /books` endpoint that retrieves all books from the database and a `GET /books/{book_id}` endpoint that retrieves a single book by ID.

#### Requirements
Completed program should:

- `GET /books` returns a list of all books in the database
- `GET /books/{book_id}` returns a specific book by ID
- Return a 404 error (using `HTTPException`) if a book with the given ID is not found
- Return an empty list if no books exist

Example responses:
```json
[
  { "id": 1, "title": "1984", "author": "George Orwell", "year": 1949 },
  { "id": 2, "title": "Brave New World", "author": "Aldous Huxley", "year": 1932 }
]
```

### 🛠️ Implement the UPDATE and DELETE Endpoints

#### Description
Add a `PUT /books/{book_id}` endpoint to update book information and a `DELETE /books/{book_id}` endpoint to remove a book from the database.

#### Requirements
Completed program should:

- `PUT /books/{book_id}` accepts a `BookCreate` body and updates the book's fields
- Return the updated book after committing changes to the database
- `DELETE /books/{book_id}` removes the book from the database
- Return a 200 response with a confirmation message
- Return a 404 error if the book ID is not found for both endpoints
