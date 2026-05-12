from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# --- Database Setup ---
DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()


# --- Database Model ---
class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    year = Column(Integer)


# --- Pydantic Models ---
class BookCreate(BaseModel):
    title: str
    author: str
    year: int


class BookResponse(BookCreate):
    id: int
    
    class Config:
        from_attributes = True


# --- Create tables on startup ---
Base.metadata.create_all(bind=engine)


# --- Dependency to get database session ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# TODO: Task 1 — Verify the database model and Pydantic models are set up correctly


# TODO: Task 2 — Implement POST /books endpoint
# Accept BookCreate body, save to database, return BookResponse


# TODO: Task 3 — Implement GET /books and GET /books/{book_id} endpoints
# GET /books returns all books
# GET /books/{book_id} returns a specific book or 404 if not found


# TODO: Task 4 — Implement PUT /books/{book_id} and DELETE /books/{book_id} endpoints
# PUT updates the book and returns the updated record
# DELETE removes the book and returns a confirmation message
