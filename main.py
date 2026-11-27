
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

# -----------------------------
# DATA STORAGE
# -----------------------------

students = []
users = []


# -----------------------------
# HELPER FUNCTIONS
# -----------------------------

def is_non_empty_text(value):
    return isinstance(value, str) and value.strip() != ""


def find_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def find_user(name):
    for user in users:
        if user["name"].lower() == name.strip().lower():
            return user
    return None


def valid_positive_integer(value):
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


# -----------------------------
# WEBSITE HOME PAGE
# -----------------------------

@app.get("/")
def welcome():
    website_file = Path(__file__).parent / "index.html"

    if website_file.exists():
        return FileResponse(str(website_file))

    return {"error": "index.html was not found. Put it in the same folder as main.py."}


# -----------------------------
# STUDENT MANAGEMENT
# -----------------------------

# GET: View all students
@app.get("/all_students")
def get_all_students():
    return students


# POST: Add a student
@app.post("/add_student")
def add_student(student: dict):

    if "id" not in student or "name" not in student or \
       "age" not in student or "course" not in student:
        return {"error": "Please provide ID, name, age and course."}

    student_id = student["id"]
    name = student["name"]
    age = student["age"]
    course = student["course"]

    if not valid_positive_integer(student_id):
        return {"error": "Student ID must be a positive whole number."}

    if not is_non_empty_text(name):
        return {"error": "Student name cannot be empty."}

    if not valid_positive_integer(age):
        return {"error": "Age must be a positive whole number."}

    if not is_non_empty_text(course):
        return {"error": "Course cannot be empty."}

    if find_student(student_id) is not None:
        return {"error": "A student with this ID already exists."}

    new_student = {
        "id": student_id,
        "name": name.strip(),
        "age": age,
        "course": course.strip()
    }

    students.append(new_student)

    return {"message": "Student added successfully."}


# GET: Search for a student by ID
@app.get("/search_student")
def search_student(student_id: int):

    if student_id <= 0:
        return {"error": "Student ID must be positive."}

    student = find_student(student_id)

    if student is None:
        return {"error": "Student not found."}

    return student


# GET: Filter students by name or course
@app.get("/filter_students")
def filter_students(keyword: str):

    if not is_non_empty_text(keyword):
        return {"error": "Please enter a search keyword."}

    matching_students = []

    for student in students:
        if keyword.strip().lower() in student["name"].lower() or \
           keyword.strip().lower() in student["course"].lower():
            matching_students.append(student)

    if len(matching_students) == 0:
        return {"message": "No matching students found."}

    return matching_students


# PUT: Replace all editable student information
@app.put("/update_student/{student_id}")
def update_student(student_id: int, updated_student: dict):

    if student_id <= 0:
        return {"error": "Student ID must be positive."}

    if "name" not in updated_student or \
       "age" not in updated_student or \
       "course" not in updated_student:
        return {"error": "Name, age and course are required."}

    name = updated_student["name"]
    age = updated_student["age"]
    course = updated_student["course"]

    if not is_non_empty_text(name):
        return {"error": "Name cannot be empty."}

    if not valid_positive_integer(age):
        return {"error": "Age must be a positive whole number."}

    if not is_non_empty_text(course):
        return {"error": "Course cannot be empty."}

    student = find_student(student_id)

    if student is None:
        return {"error": "Student not found."}

    student["name"] = name.strip()
    student["age"] = age
    student["course"] = course.strip()

    return {"message": "Student updated successfully."}


# PATCH: Update only the fields supplied
@app.patch("/patch_student/{student_id}")
def patch_student(student_id: int, student_data: dict):

    if student_id <= 0:
        return {"error": "Student ID must be positive."}

    if len(student_data) == 0:
        return {"error": "Please provide at least one field to update."}

    allowed_fields = ["name", "age", "course"]

    for field in student_data:
        if field not in allowed_fields:
            return {"error": "Only name, age and course can be updated."}

    if "name" in student_data:
        if not is_non_empty_text(student_data["name"]):
            return {"error": "Name cannot be empty."}

    if "age" in student_data:
        if not valid_positive_integer(student_data["age"]):
            return {"error": "Age must be a positive whole number."}

    if "course" in student_data:
        if not is_non_empty_text(student_data["course"]):
            return {"error": "Course cannot be empty."}

    student = find_student(student_id)

    if student is None:
        return {"error": "Student not found."}

    for field in student_data:
        if field == "name" or field == "course":
            student[field] = student_data[field].strip()
        else:
            student[field] = student_data[field]

    return {"message": "Student information partially updated."}


# DELETE: Delete a student
@app.delete("/delete_student/{student_id}")
def delete_student(student_id: int):

    if student_id <= 0:
        return {"error": "Student ID must be positive."}

    student = find_student(student_id)

    if student is None:
        return {"error": "Student not found."}

    students.remove(student)

    return {"message": "Student deleted successfully."}


# -----------------------------
# USER ACCOUNT MANAGEMENT
# -----------------------------

# POST: Create an account
@app.post("/signup")
def signup(user: dict):

    if "name" not in user or "password" not in user or \
       "secret_word" not in user:
        return {"error": "Name, password and secret word are required."}

    name = user["name"]
    password = user["password"]
    secret_word = user["secret_word"]

    if not is_non_empty_text(name):
        return {"error": "Name cannot be empty."}

    if not is_non_empty_text(password):
        return {"error": "Password cannot be empty."}

    if len(password) < 6:
        return {"error": "Password must contain at least 6 characters."}

    if not is_non_empty_text(secret_word):
        return {"error": "Secret word cannot be empty."}

    if find_user(name) is not None:
        return {"error": "This account name is already registered."}

    new_user = {
        "name": name.strip(),
        "password": password,
        "secret_word": secret_word.strip()
    }

    users.append(new_user)

    return {"message": "Account created successfully. You can now log in."}


# POST: Login
@app.post("/login")
def login(user: dict):

    if "name" not in user or "password" not in user:
        return {"error": "Name and password are required."}

    name = user["name"]
    password = user["password"]

    if not is_non_empty_text(name) or not is_non_empty_text(password):
        return {"error": "Name and password cannot be empty."}

    account = find_user(name)

    if account is None:
        return {"error": "Account name not found."}

    if account["password"] != password:
        return {"error": "Incorrect password."}

    return {"message": "Login successful."}


# POST: Verify account for forgot password
@app.post("/forgot_password")
def forgot_password(user: dict):

    if "name" not in user or "secret_word" not in user:
        return {"error": "Name and secret word are required."}

    name = user["name"]
    secret_word = user["secret_word"]

    if not is_non_empty_text(name) or not is_non_empty_text(secret_word):
        return {"error": "Name and secret word cannot be empty."}

    account = find_user(name)

    if account is None:
        return {"error": "Account name not found."}

    if account["secret_word"].lower() != secret_word.strip().lower():
        return {"error": "Incorrect secret word."}

    return {"message": "Account verified. You may now reset your password."}


# PUT: Reset password
@app.put("/reset_password")
def reset_password(user: dict):

    if "name" not in user or "secret_word" not in user or \
       "new_password" not in user:
        return {"error": "Name, secret word and new password are required."}

    name = user["name"]
    secret_word = user["secret_word"]
    new_password = user["new_password"]

    if not is_non_empty_text(name):
        return {"error": "Name cannot be empty."}

    if not is_non_empty_text(secret_word):
        return {"error": "Secret word cannot be empty."}

    if not is_non_empty_text(new_password):
        return {"error": "New password cannot be empty."}

    if len(new_password) < 6:
        return {"error": "New password must contain at least 6 characters."}

    account = find_user(name)

    if account is None:
        return {"error": "Account name not found."}

    if account["secret_word"].lower() != secret_word.strip().lower():
        return {"error": "Incorrect secret word."}

    account["password"] = new_password

    return {
        "message": "Password reset successfully. Please log in with your new password."
    }
