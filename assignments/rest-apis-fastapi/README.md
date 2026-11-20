# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI to practice HTTP methods, route parameters, request validation, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description

Set up a FastAPI application for managing a collection of books. Define a data model for each book and add an endpoint that confirms the API is running.

#### Requirements

Completed program should:

- Create a FastAPI application instance.
- Define a `Book` model with a title, author, and publication year.
- Add a `GET /` endpoint that returns a welcome message.
- Store books in an in-memory collection for this assignment.

### 🛠️ Implement Book Endpoints

#### Description

Implement CRUD endpoints that allow clients to create, read, update, and delete books through the API.

#### Requirements

Completed program should:

- Add `GET /books` to return all books.
- Add `GET /books/{book_id}` to return one book or a `404` response when it does not exist.
- Add `POST /books` to validate and create a new book.
- Add `PUT /books/{book_id}` to update an existing book.
- Add `DELETE /books/{book_id}` to remove an existing book.
- Use appropriate HTTP status codes and verify the endpoints through FastAPI's interactive documentation at `/docs`.
