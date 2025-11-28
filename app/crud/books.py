from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app import models, schemas

router = APIRouter()

# Create Book
@router.post("/books", response_model=schemas.BookOut)
def create_book(payload: schemas.BookCreate, db: Session = Depends(get_db)):
    book = models.Book(
        title=payload.title,
        content=payload.content,
        author_name=payload.author_name
        
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

# list All Books
@router.get("/books", response_model=list[schemas.BookOut])
def list_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

# Read Single Book
@router.get("/books/{book_id}", response_model=schemas.BookOut)
def get_books(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="book not found")
    return book

# Update Book
@router.put("/books/{book_id}", response_model=schemas.BookOut)
def update_book(book_id: int, payload: schemas.BookCreate, db: Session = Depends(get_db)):
    book = db.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="book not found")

    book.title = payload.title
    book.content = payload.content
    book.author_name = payload.author_name

    db.commit()
    db.refresh(book)
    return book
# Delete Book
@router.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="book not found")

    db.delete(book)
    db.commit()
    return {"msg": "deleted"}