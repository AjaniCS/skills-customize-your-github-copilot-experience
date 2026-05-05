# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, high-performance REST APIs using the FastAPI framework! You'll master creating endpoints, handling HTTP methods, and validating user data with Pydantic. By the end of this assignment, you'll understand how web services communicate with clients and how to structure backend applications for real-world applications.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Start by setting up a FastAPI application and building your first API endpoint. You'll create a simple "Hello" endpoint that responds to HTTP requests. This foundational task teaches you how FastAPI works, how to run a development server, and how HTTP requests and responses flow through your application.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Define a GET endpoint at the root path (`/`) that returns a JSON response
- Include a simple greeting message and a timestamp or id field
- Run the development server without errors using `uvicorn`

---

### 🛠️ Add Multiple Endpoints with Different HTTP Methods

#### Description
Expand your API to handle different HTTP methods and routes. You'll create endpoints for GET (retrieve data), POST (create data), and learn how to work with URL parameters and request bodies. This task demonstrates how real APIs handle different types of client requests and structure multiple operations.

#### Requirements
Completed program should:

- Include at least 3 endpoints (GET, POST, and another GET with parameters)
- Define a GET endpoint that retrieves items (e.g., `/items` returns a list)
- Define a GET endpoint with path parameters (e.g., `/items/{item_id}`)
- Define a POST endpoint that accepts JSON data and returns the created item
- Return appropriate HTTP status codes for each endpoint

---

### 🛠️ Implement Data Validation with Pydantic Models

#### Description
Learn professional API design by adding Pydantic models for request and response validation. You'll define data schemas, validate incoming data automatically, and ensure your API contract is clear and enforced. This protects your application from invalid data and provides automatic API documentation.

#### Requirements
Completed program should:

- Define at least one Pydantic model for request/response data (e.g., Item, User)
- Use the model in a POST endpoint to validate incoming JSON
- Include data validation rules (required fields, field types, optional fields)
- Return responses that match the Pydantic model structure
- Access the auto-generated interactive API docs at `/docs` endpoint

---

### 🛠️ (Stretch) Add Error Handling and Status Codes

#### Description
Write production-ready code by implementing proper error handling and HTTP status codes. You'll catch validation errors, handle missing resources, and return meaningful error messages to clients. This makes your API robust and user-friendly.

#### Requirements
Completed program should:

- Return 404 status when requested items don't exist
- Return 400 status for invalid request data
- Raise HTTPException with appropriate status codes and detail messages
- Handle edge cases gracefully without crashing
- Provide meaningful error messages to API clients
