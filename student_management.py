import json
def add_student():
    name = input("\033[1;32mEnter student name: \033[0m")
    age = input("\033[1;32mEnter student age: \033[0m")
    mark = input("\033[1;32mEnter student mark: \033[0m")
    grade = input("\033[1;32mEnter student grade: \033[0m")
    
    student = {
        "name": name,
        "age": age,
        "mark": mark,
        "grade": grade
    }
    
    with open('students.txt', 'a') as file:
        file.write(json.dumps(student))
        file.write('\n')
    
    print("Student added successfully!")

          
 
def view_students():
    try:
        with open('students.txt', 'r') as file:
            
            print("\nList of Students:")
            for line in file:
                student = json.loads(line)
                print(f"Name: {student['name']}, Age: {student['age']}, Mark: {student['mark']}, Grade: {student['grade']}")
    except FileNotFoundError:
        print("No students found. Please add students first.")
def search_student():
    search_name = input("\033[1;34mEnter the name of the student to search:\033[0m ")
    try:
        with open('students.txt', 'r') as file:
            found = False
            for line in file:
                student = json.loads(line)
                if student['name'].lower() == search_name.lower():
                    print(f"Name: {student['name']}, Age: {student['age']}, Mark: {student['mark']}, Grade: {student['grade']}")
                    found = True
                    break
            if not found:
                print("Student not found.")
    except FileNotFoundError:
        print("No students found. Please add students first.")        
#main menu
while True:
    print("\033[1;33m\n========= student mangement system:======\033[0m")
    print("\033[1;32m1. Add student\033[0m")
    print("\033[1;32m2. View students\033[0m")
    print("\033[1;32m3. Search student\033[0m")
    print("\033[1;32m4. Exit\033[0m")

    choice = input("\033[1;34mEnter your choice: \033[0m")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        print("\033[1;31mExiting the program.\033[0m")
        break
    else:
        print("\033[1;37mInvalid choice. Please try again.\033[0m")
