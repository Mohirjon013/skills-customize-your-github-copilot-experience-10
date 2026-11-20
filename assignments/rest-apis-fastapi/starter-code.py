from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Book API")


class Book(BaseModel):
    title: str
    author: str
    publication_year: int


books: dict[int, Book] = {}


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API"}


# TODO: Add GET /books to return all books.

# TODO: Add GET /books/{book_id} to return one book or a 404 response.

# TODO: Add POST /books to validate and store a new book.

# TODO: Add PUT /books/{book_id} to update an existing book.

# TODO: Add DELETE /books/{book_id} to remove an existing book.
