from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# --- Sample data ---
students = {
    1: {"id": 1, "name": "Alex Johnson"},
    2: {"id": 2, "name": "Maria Garcia"},
}

assignments = []


# --- Pydantic model ---
class Assignment(BaseModel):
    title: str
    due_date: str


# TODO: Task 1 — Define a GET / endpoint that returns a welcome message


# TODO: Task 2 — Define a GET /students/{student_id} endpoint
# Return the student dict if found, raise HTTPException(status_code=404) if not


# TODO: Task 3 — Define a POST /assignments endpoint that accepts an Assignment body
# Append the assignment to the assignments list and return a confirmation


# TODO: Task 4 — Define a GET /assignments endpoint that returns all stored assignments
