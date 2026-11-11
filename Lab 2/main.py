students = {}

def add_student():
    sid = input("Student ID: ")
    name = input("Student Name: ")
    students[sid] = {"name": name, "courses": set()}
    print("Student added!")

def register_course():
    sid = input("Student ID: ")
    if sid in students:
        students[sid]["courses"].add(input("Course Name: "))
        print("Course registered!")
    else:
        print("Student not found!")

def drop_course():
    sid = input("Student ID: ")
    if sid in students:
        course = input("Course Name: ")
        students[sid]["courses"].discard(course)
        print("Course dropped!")
    else:
        print("Student not found!")

def search_student():
    sid = input("Student ID: ")
    if sid in students:
        print(students[sid])
    else:
        print("Student not found!")

def unique_courses():
    courses = {c for s in students.values() for c in s["courses"]}
    print("Unique Courses:", courses)

def shared_course():
    course = input("Course Name: ")
    for sid, s in students.items():
        if course in s["courses"]:
            print(sid, s["name"])

def display_students():
    for sid, s in sorted(students.items(), key=lambda x: x[1]["name"]):
        print(sid, s["name"], s["courses"])


while True:
    print("\n1. Add Student")
    print("2. Register Course")
    print("3. Drop Course")
    print("4. Search Student")
    print("5. Unique Courses")
    print("6. Find Students Sharing Course")
    print("7. Display Students")
    print("8. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        register_course()
    elif choice == "3":
        drop_course()
    elif choice == "4":
        search_student()
    elif choice == "5":
        unique_courses()
    elif choice == "6":
        shared_course()
    elif choice == "7":
        display_students()
    elif choice == "8":
        break
    else:
        print("Invalid choice!")