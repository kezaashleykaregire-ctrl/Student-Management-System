from fastapi import FastAPI

app = FastAPI()


students = [
    {"id": 1, "name": "Tobby", "age": 20, "course": "IT"},
    {"id": 2, "name": "Celine", "age": 21, "course": "Business"},
    {"id": 3, "name": "Enzo", "age": 22, "course": "Computer Science"}
]

users = []

@app.get("/")
def welcome():
    return  {"message": "Welcome to Student Management System"}

@app.get("/all_students")
def get_all_students():
    return students

@app.post("/add_student")
def add_student(student:dict):

    if "id" not in student or "name" not in student or "age" not in student or "course" not in student:
        return {"error": "All fields are required:id, name, age, course"}

    if type(student["id"]) != int or type(student["age"]) != int:
        return {"error":"ID and age must be numbers"}

    if type(student["name"]) != str or type(student["course"]) !=str:
        return {"error": "Name and course must be text"}


    if student["age"] <= 0:
        return {"error": "Age must be greater than 0"}


    for existing_student in students:
        if existing_student["id"] == student["id"]:
            return {"error": "Student ID already exists"}

    students.append(student)

    return {"message": "Student added successfully"}

@app.get("/search_student")
def search_student(student_id: int):
    for student in students:

    
        if student["id"] == student_id:
            return student

    
    return {"error": "Student not found"}

@app.put("/update_student/{student_id}")
def update_student(student_id: int, updated_student: dict):


    if "name" not in updated_student or "age" not in updated_student or "course" not in updated_student:
        return {"error": "Name, age and course are required"}


    if type(updated_student["name"]) != str or type(updated_student["course"]) != str:
        return {"error": "Name and course must be text"}

    if type(updated_student["age"]) != int:
        return {"error": "Age must be a number"}

    if updated_student["age"] <= 0:
        return {"error": "Age must be greater than 0"}


    for student in students:
        if student["id"] == student_id:

        
            student["name"] = updated_student["name"]
            student["age"] = updated_student["age"]
            student["course"] = updated_student["course"]

            return {"message": "Student updated successfully"}

    return {"error": "Student not found"}


@app.patch("/patch_student/{student_id}")
def patch_student(student_id: int, student_data: dict):


    if len(student_data) == 0:
        return {"error": "Provide at least one field to update"}


    for field in student_data:
        if field not in ["name", "age", "course"]:
            return {"error": "Only name, age and course can be updated"}


    if "name" in student_data:
        if type(student_data["name"]) != str or student_data["name"].strip() == "":
            return {"error": "Name must be valid text"}


    if "age" in student_data:
        if type(student_data["age"]) != int or student_data["age"] <= 0:
            return {"error": "Age must be a positive number"}
        
    if "course" in student_data:
        if type(student_data["course"]) != str or student_data["course"].strip() == "":
            return {"error": "Course must be valid text"}


    for student in students:
        if student["id"] == student_id:

        
            for field in student_data:
                student[field] = student_data[field]

            return {"message": "Student information updated successfully"}

    return {"error": "Student not found"}


@app.delete("/delete_student/{student_id}")
def delete_student(student_id: int):


    for student in students:


        if student["id"] == student_id:


            students.remove(student)

            return {"message": "Student deleted successfully"}


    return {"error": "Student not found"}


@app.get("/filter_students")
def filter_students(keyword: str):


    if keyword.strip() == "":
        return {"error": "Please enter a search keyword"}


    results = []


    for student in students:

    
        if keyword.lower() in student["name"].lower() or keyword.lower() in student["course"].lower():
            results.append(student)


    if len(results) == 0:
        return {"message": "No matching students found"}

    return results


@app.post("/signup")
def signup(user: dict):


    if "name" not in user or "password" not in user or "secret_word" not in user:
        return {"error": "Name, password and secret word are required"}


    if type(user["name"]) != str or type(user["password"]) != str or type(user["secret_word"]) != str:
        return {"error": "All fields must contain text"}


    if user["name"].strip() == "" or user["password"] == "" or user["secret_word"].strip() == "":
        return {"error": "Fields cannot be empty"}


    if len(user["password"]) < 6:
        return {"error": "Password must contain at least 6 characters"}


    for existing_user in users:
        if existing_user["name"].lower() == user["name"].lower():
            return {"error": "This student name is already registered"}
        
    users.append(user)

    return {"message": "Student registered successfully"}



@app.post("/login")
def login(user: dict):


    if "name" not in user or "password" not in user:
        return {"error": "Name and password are required"}


    if type(user["name"]) != str or type(user["password"]) != str:
        return {"error": "Name and password must be text"}


    if user["name"].strip() == "" or user["password"] == "":
        return {"error": "Name and password cannot be empty"}


    for existing_user in users:

        if existing_user["name"].lower() == user["name"].lower():

            if existing_user["password"] == user["password"]:
                return {"message": "Login successful"}

            else:
                return {"error": "Incorrect password"}

    return {"error": "Student not found"}


@app.post("/forgot_password")
def forgot_password(user: dict):

  
    if "name" not in user or "secret_word" not in user:
        return {"error": "Name and secret word are required"}

    
    if type(user["name"]) != str or type(user["secret_word"]) != str:
        return {"error": "Name and secret word must be text"}

    
    if user["name"].strip() == "" or user["secret_word"].strip() == "":
        return {"error": "Fields cannot be empty"}

    
    for existing_user in users:

        if existing_user["name"].lower() == user["name"].lower():


            if existing_user["secret_word"] == user["secret_word"]:
                return {"message": "Account verified. You can reset your password"}

            else:
                return {"error": "Incorrect secret word"}

    return {"error": "Student not found"}


@app.put("/reset_password")
def reset_password(user: dict):


    if "name" not in user or "secret_word" not in user or "new_password" not in user:
        return {"error": "Name, secret word and new password are required"}


    if type(user["name"]) != str or type(user["secret_word"]) != str or type(user["new_password"]) != str:
        return {"error": "All fields must contain text"}

  
    if user["name"].strip() == "" or user["secret_word"].strip() == "" or user["new_password"] == "":
        return {"error": "Fields cannot be empty"}

  
    if len(user["new_password"]) < 6:
        return {"error": "New password must contain at least 6 characters"}

    
    for existing_user in users:

        if existing_user["name"].lower() == user["name"].lower():


            if existing_user["secret_word"] == user["secret_word"]:

                existing_user["password"] = user["new_password"]

                return {"message": "Password reset successfully"}

            else:
                return {"error": "Incorrect secret word"}

    return {"error": "Student not found"}
