# 📘 Assignment: Building CRUD APIs with FastAPI and SQLite

## 🎯 Objective

Learn how to build a persistent backend by creating a CRUD API with FastAPI and SQLite. You will practice defining API routes, working with a database, validating data with Pydantic, and handling HTTP responses for real-world applications.

## 📝 Tasks

### 🛠️ Set Up the FastAPI Application

#### Description
Create the basic FastAPI app and build a root endpoint. This task introduces the web framework, how to start the server, and how HTTP requests are handled by your application.

#### Requirements
Completed program should:

- Create a `FastAPI` app instance
- Add a GET endpoint at `/` that returns a welcome message
- Verify the app starts successfully with `uvicorn`
- Confirm that the interactive docs are available at `/docs`

---

### 🛠️ Add SQLite Persistence

#### Description
Connect your API to a SQLite database and create a table for storing items. This task shows how to persist data across requests and store application state in a lightweight database.

#### Requirements
Completed program should:

- Connect to a SQLite database file
- Create a table if it does not exist
- Use a Pydantic model to represent stored data
- Initialize the database when the app starts

---

### 🛠️ Implement Full CRUD Endpoints

#### Description
Build the core create, read, update, and delete API routes for your database-backed resource. This teaches students how to map HTTP methods to database operations and create a complete service.

#### Requirements
Completed program should:

- Implement a POST endpoint to create a new item
- Implement a GET endpoint to list all items
- Implement a GET endpoint to retrieve one item by ID
- Implement a PUT or PATCH endpoint to update an item by ID
- Implement a DELETE endpoint to remove an item by ID

---

### 🛠️ Add Validation and Error Handling

#### Description
Make the API robust by validating incoming data and handling errors clearly. Students will learn to return proper HTTP status codes and informative error messages for invalid requests and missing records.

#### Requirements
Completed program should:

- Validate incoming request data with Pydantic models
- Return `404` when a requested item does not exist
- Return `400` for invalid request data
- Use `HTTPException` with clear detail messages
- Keep the API stable without crashing on bad input
