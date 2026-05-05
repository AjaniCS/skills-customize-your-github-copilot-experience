"""
FastAPI CRUD API Starter Code

Complete the tasks by adding database persistence and CRUD endpoints.
"""

import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from pathlib import Path

DB_FILE = Path(__file__).parent / "items.db"

# Initialize the FastAPI app
app = FastAPI(title="FastAPI CRUD with SQLite", version="1.0.0")

# Pydantic models for request and response validation
class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ItemResponse(ItemCreate):
    id: int


def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    with get_db_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL
            )
            """
        )


@app.on_event("startup")
async def startup_event():
    create_table()


@app.get("/", response_model=dict)
async def root():
    return {"message": "Welcome to your FastAPI CRUD API", "status": "ready"}


# TODO: Add your CRUD endpoints below
# - POST /items to create a new item
# - GET /items to list all items
# - GET /items/{item_id} to retrieve one item
# - PUT /items/{item_id} to update an item
# - DELETE /items/{item_id} to remove an item


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
