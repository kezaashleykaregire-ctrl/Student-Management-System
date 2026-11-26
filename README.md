
# Student Management System

## 1. Project Description

The Student Management System is a Python backend application built using FastAPI.

It allows users to manage student records and perform different operations such as adding, viewing, searching, filtering, updating, and deleting students.

It also includes account features such as signup, login, forgot password, and reset password.

## 2. Technologies Used

- Python
- FastAPI
- Uvicorn
- Visual Studio Code
- Postman

## 3. Installation

Make sure Python is installed on your computer.

Install the required packages by running:

```bash
py -m pip install -r requirements.txt
```

## 4. How to Run the Project

Open the terminal inside the project folder and run:

```bash
py -m uvicorn main:app --reload
```

The application will run at:

http://127.0.0.1:8000

You can also view the API documentation at:

http://127.0.0.1:8000/docs

## 5. Student Management Features

- View all students
- Search for a student using their ID
- Filter students by name or course
- Add a new student
- Update a student's full record
- Partially update a student's information
- Delete a student

## 6. Account Features

- Register a new account
- Login
- Verify an account using a secret word
- Reset a password

## 7. HTTP Methods Used

| Method | Purpose |
|---|---|
| GET | Retrieve student records |
| POST | Add students and register or log in |
| PUT | Fully update a student or reset a password |
| PATCH | Partially update a student |
| DELETE | Delete a student |

## 8. Data Storage

The project uses Python lists and dictionaries to store student and user information in memory.

Data is reset when the application restarts.

## 9. Testing

The API endpoints were tested using Postman.

The Postman collection is included in this project:

Student_Management_System_Postman.json
