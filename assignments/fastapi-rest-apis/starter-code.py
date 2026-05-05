"""
FastAPI REST API Starter Code

This is your starting point for building REST APIs with FastAPI.
Complete the tasks by adding endpoints, models, and error handling.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# Initialize the FastAPI app
app = FastAPI(title="Learning REST APIs", version="1.0.0")

# ============================================================================
# TODO: Define a Pydantic model for your data (Task 3)
# Example structure:
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None
#     price: float
# ============================================================================


# ============================================================================
# TODO: Add your API endpoints here
# Task 1: Create a basic GET endpoint at "/"
# Task 2: Add GET, POST, and parameterized endpoints
# Task 3: Use your Pydantic models for validation
# Task 4: Add error handling with HTTPException
# ============================================================================

@app.get("/")
async def root():
    """
    Welcome endpoint - returns a greeting.
    This is your starting point. Add more endpoints below!
    """
    return {
        "message": "Welcome to your FastAPI application!",
        "timestamp": datetime.now().isoformat()
    }


# Add more endpoints here following the structure above
# Remember to use appropriate HTTP methods (GET, POST, PUT, DELETE)
# and validate data with Pydantic models!


if __name__ == "__main__":
    import uvicorn
    # Run with: python starter-code.py
    # Then visit: http://127.0.0.1:8000/docs
    uvicorn.run(app, host="127.0.0.1", port=8000)
