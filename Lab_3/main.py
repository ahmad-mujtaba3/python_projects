import json
import os

FILE = "students.json"

def load():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save():
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

students = load()

def add():
    sid = input("Student ID: ")
    if not sid or sid in students:
        print("Invalid or existing ID!")
        return

    name = input("Name: ")
    dept = input("Department: ")
    sem = input("Semester: ")

    if not name or not dept or not sem:
        print("All fields are required!")
        return

    students[sid] = {
        "name": name,
        "department": dept,
        "semester": sem
    }
    save()
    print("Student added!")

def display():
    for sid, s in students.items():
        print(sid, s)

def search():
    sid = input("Student ID: ")
    print(students.get(sid, "Student not found!"))

def update():
    sid = input("Student ID: ")
    if sid in students:
        students[sid]["name"] = input("New Name: ")
        students[sid]["department"] = input("New Department: ")
        students[sid]["semester"] = input("New Semester: ")
        save()
        print("Updated!")
    else:
        print("Student not found!")

def delete():
    sid = input("Student ID: ")
    if sid in students:
        del students[sid]
        save()
        print("Deleted!")
    else:
        print("Student not found!")

while True:
    print("\n1. Add Student")
    print("2. List Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add()
    elif choice == "2":
        display()
    elif choice == "3":
        search()
    elif choice == "4":
        update()
    elif choice == "5":
        delete()
    elif choice == "6":
        break
    else:
        print("Invalid choice!")