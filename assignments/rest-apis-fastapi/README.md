# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using the FastAPI framework by creating endpoints that handle HTTP requests, validate data, and return structured JSON responses.

## 📝 Tasks

### 🛠️ Set Up a FastAPI Application

#### Description
Create a basic FastAPI application with a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import and initialize a `FastAPI` app instance
- Define a `GET /` endpoint that returns a JSON response with a `message` field
- Run the app using `uvicorn` (e.g., `uvicorn main:app --reload`)

Example output when calling `GET /`:
```json
{ "message": "Welcome to the Homework API!" }
```

### 🛠️ Add a Students Endpoint with Path Parameters

#### Description
Extend the API with a `/students/{student_id}` endpoint that returns information about a student based on their ID.

#### Requirements
Completed program should:

- Define a `GET /students/{student_id}` endpoint that accepts a path parameter `student_id` (integer)
- Return a JSON object with at least `id` and `name` fields for the requested student
- Return a meaningful error response (using `HTTPException`) if the student ID is not found

Example output when calling `GET /students/1`:
```json
{ "id": 1, "name": "Alex Johnson" }
```

### 🛠️ Create an Endpoint That Accepts Data

#### Description
Add a `POST /assignments` endpoint that accepts a JSON body and stores a new assignment entry.

#### Requirements
Completed program should:

- Define a Pydantic model (e.g., `Assignment`) with at least `title` (str) and `due_date` (str) fields
- Define a `POST /assignments` endpoint that accepts the model as a request body
- Return the created assignment with a confirmation message

Example request body:
```json
{ "title": "Python Basics", "due_date": "2026-05-20" }
```

Example response:
```json
{ "message": "Assignment created", "assignment": { "title": "Python Basics", "due_date": "2026-05-20" } }
```

### 🛠️ List All Assignments

#### Description
Add a `GET /assignments` endpoint that returns all assignments that have been submitted via `POST /assignments` during the current session.

#### Requirements
Completed program should:

- Store submitted assignments in an in-memory list
- Define a `GET /assignments` endpoint that returns all stored assignments as a JSON array
- Return an empty array if no assignments have been added yet
