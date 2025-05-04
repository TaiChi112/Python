from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# ----------------------
# Schema (Pydantic model)
# ----------------------
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int] = None

# ----------------------
# Fake Database (List)
# ----------------------
books: List[Book] = []

# ----------------------
# CRUD Routes
# ----------------------

# Create
@app.post("/books", response_model=Book)
def create_book(book: Book):
    for b in books:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book with this ID already exists.")
    books.append(book)
    return book

# Read all
@app.get("/books", response_model=List[Book])
def get_books():
    return books

# Read one
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Update
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for idx, book in enumerate(books):
        if book.id == book_id:
            books[idx] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# Delete
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for idx, book in enumerate(books):
        if book.id == book_id:
            books.pop(idx)
            return {"message": f"Book with id {book_id} deleted."}
    raise HTTPException(status_code=404, detail="Book not found")
