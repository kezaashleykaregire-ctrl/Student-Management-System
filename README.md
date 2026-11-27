# Student Management System

## 1. Project Description

The Student Management System is a web-based application developed using Python and FastAPI. It allows users to create accounts, log in, recover forgotten passwords, and manage student records.

The system provides a simple website interface where users can add, view, search, filter, update, and delete student information.

## 2. Project Objectives

- To make student record management easier.
- To practise using Python and FastAPI.
- To understand how a frontend communicates with a backend.
- To practise creating and testing API endpoints.
- To apply Python concepts such as variables, lists, dictionaries, conditions, loops, and functions.

## 3. Technologies Used

- **Python:** Main programming language.
- **FastAPI:** Backend framework.
- **HTML:** Website structure.
- **CSS:** Website styling.
- **JavaScript:** Website functionality and communication with the backend.
- **Uvicorn:** Runs the FastAPI application.
- **Visual Studio Code:** Code editor.
- **Postman:** API testing tool.
- **GitHub:** Project storage and version control.

## 4. Main Features

### Account Management
- Create a new account.
- Log in using an account name and password.
- Prevent duplicate account names.
- Recover a forgotten password using a secret word.
- Reset an account password.

### Student Management
- Add a new student.
- View all registered students.
- Search for a student using their ID.
- Filter students by name or course.
- Update student information.
- Delete student records.

## 5. Project Folder Structure

```text
Student_Management_System/
│
├── main.py
├── index.html
├── requirements.txt
├── Student_Management_System_Postman.json
└── README.md
```

## 6. Installation Requirements

Make sure Python is installed on your computer.

Open the VS Code terminal in the project folder and install the required packages:

```bash
py -m pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
fastapi
uvicorn
```

## 7. How to Run the Project

1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Make sure the terminal is inside the folder containing `main.py`.
4. Run the following command:

```bash
py -m uvicorn main:app --reload
```

5. Open your browser.
6. Visit the website:

```text
http://127.0.0.1:8000
```

To view and test the API documentation, visit:

```text
http://127.0.0.1:8000/docs
```

Keep the terminal running while using the website.

## 8. API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Opens the website |
| GET | `/all_students` | Displays all students |
| POST | `/add_student` | Adds a student |
| GET | `/search_student` | Searches by student ID |
| GET | `/filter_students` | Filters students |
| PUT | `/update_student/{student_id}` | Updates all student details |
| PATCH | `/patch_student/{student_id}` | Updates selected student details |
| DELETE | `/delete_student/{student_id}` | Deletes a student |
| POST | `/signup` | Creates an account |
| POST | `/login` | Logs into an account |
| POST | `/forgot_password` | Verifies account recovery details |
| PUT | `/reset_password` | Resets an account password |

## 9. Data Storage

The application uses Python lists and dictionaries to store student and account information.

The data is stored temporarily while the application is running. It is not stored in a permanent database, so the records are reset when the server restarts.

## 10. Testing

Postman is used to test the API endpoints.

Testing includes:

- Adding students successfully.
- Searching for existing and non-existing students.
- Filtering student records.
- Updating student information.
- Deleting student records.
- Creating accounts and logging in.
- Testing password recovery and password resetting.
- Checking invalid inputs and missing information.
- Checking duplicate student IDs and account names.

The Postman collection is included in the project folder.

## 11. Limitations

- Student and account information is stored temporarily in memory.
- Data is lost when the server restarts.
- The project is designed for educational purposes and is not intended for production use.

## 12. Conclusion

The Student Management System demonstrates how Python, FastAPI, HTML, CSS, and JavaScript can work together to create a simple web application.

The project helped develop practical skills in programming, API development, data management, frontend development, and software testing.

---

**Project Name:** Student Management System  
**Backend:** Python FastAPI  
**Frontend:** HTML, CSS and JavaScript  
**Testing Tool:** Postman