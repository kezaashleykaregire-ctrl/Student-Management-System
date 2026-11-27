# Student Management System

## Project Description
The Student Management System is a web-based application developed using Python and FastAPI. It allows users to create accounts, log in, recover forgotten passwords, and manage student records.

## Features
- User registration (Sign Up)
- User login
- Forgot password verification using a secret word
- Password reset
- Add new students
- View all students
- Search students by ID
- Filter students by name or course
- Update student records
- Partially update student records
- Delete student records

## Technologies Used
- Python
- FastAPI
- Uvicorn
- HTML
- CSS
- JavaScript
- Postman

## Project Files
- `main.py`: Contains the FastAPI backend and application routes.
- `index.html`: Contains the website interface.
- `requirements.txt`: Lists the Python libraries required.
- `Student_Management_System_Postman.json`: Contains the exported Postman API collection.
- `README.md`: Provides information and instructions about the project.

## Installation

1. Install Python.
2. Open the project folder in VS Code.
3. Open the VS Code terminal.
4. Install the required libraries:

```bash
py -m pip install -r requirements.txt
```

## How to Run the Project

Run this command in the VS Code terminal:

```bash
py -m uvicorn main:app --reload
```

Open the website in your browser:

`http://127.0.0.1:8000`

FastAPI documentation is available at:

`http://127.0.0.1:8000/docs`

## Data Storage
The application uses Python lists and dictionaries to store student records and user accounts temporarily in memory. Data is reset when the server restarts.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Open the website |
| GET | `/all_students` | View all students |
| POST | `/add_student` | Add a student |
| GET | `/search_student` | Search by student ID |
| GET | `/filter_students` | Filter students |
| PUT | `/update_student/{student_id}` | Fully update a student |
| PATCH | `/patch_student/{student_id}` | Partially update a student |
| DELETE | `/delete_student/{student_id}` | Delete a student |
| POST | `/signup` | Register an account |
| POST | `/login` | Log in |
| POST | `/forgot_password` | Verify account recovery details |
| PUT | `/reset_password` | Reset a password |

## Testing
The API endpoints can be tested using Postman. Both successful requests and invalid-input cases should be tested.

## Author
Student Management System Project