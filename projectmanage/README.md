# Task Management API

This project is a Django-based REST API for managing tasks. It allows users to create, read, update, and delete tasks efficiently.

## Features

- User authentication
- Task creation, retrieval, updating, and deletion
- API endpoints for task management

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd task_management_api
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- The API can be accessed at `http://127.0.0.1:8000/api/`.
- Use tools like Postman or curl to interact with the API endpoints.

e welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### Endpoints

1. **GET /api/**  
   - Retrieve a list of all tasks.

2. **POST /api/**  
   - Create a new task.  
   - **Payload Example**:
     ```json
     {
         "name": "Sample Task",
         "status": "todo"
     }
     ```

3. **PUT /api/{id}/**  
   - Update an existing task.  
   - **Payload Example**:
     ```json
     {
         "name": "Updated Task",
         "status": "in_progress"
     }
     ```

4. **DELETE /api/{id}/**  
   - Delete an existing task.