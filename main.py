from StudentReportCardMngSys import School, Student

def main():
    is_running = True
    school = School()

    while is_running:
        print("\n\n1. Add new Student\n" \
            "2. Add course and grade to student\n" \
            "3. View student report\n" \
            "4. View all students\n" \
            "5. Delete a student\n" \
            "6. Show students ranking\n" \
            "7. Save data to file\n" \
            "8. Load data from file(note:loading from txt or csv will only print the data it will not recreate objects)\n" \
            "9. Exit Program\n\n")
                
        while True:
            try:
                operation = int(input("\n\nEnter the number of the operation you want: "))
                if not (0 < operation < 10):
                    raise ValueError("Please choose an option from the menu!")
            except ValueError as e:
                print(f"ValueError: {e}")
            else:
                break

        match operation:
            case 1:
                name = input("Enter the name of the student: ")
                
                while True:
                    try:
                        year = int(input("Enter the year of the student (1 to 12): "))
                        if not (1 <= year <= 12):
                            raise ValueError("choose a year (1 to 12)")
                    except ValueError as e:
                        print(f"Value Error: choose a number from options")
                    else:
                        break
                student = Student(name=name,year=year)
                school.add_student(student)
                print(f"Student {name} added successfully.")

            case 2:
                course_name = input("Enter name of the course: ")
                while True:
                    try:
                        grade = float(input("Enter the grade of this course: "))
                        if not (0 <= grade <= 100):
                            raise ValueError("enter a grade between 1 and 100!")
                    except ValueError as e:
                        print(f"Value Error: {e}")
                    else:
                        break
                st_name = input("Enter the student name to add the course to his report: ")
                student = school.find_by_name(st_name)
                if student:
                    student.add_course(course_name,grade)
                    print("Course added successfully.")
                else:
                    print(f"Student {st_name} was not found")
            case 3:
                st_name = input("Enter the student name to add the course to his report: ")
                student = school.find_by_name(st_name)
                if student:
                    report = student.get_report()
                    print(f"{report}")
                else:
                    print(f"Student {st_name} was not found")
            case 4:
                school.display_all()
            case 5:
                while True:
                    try:
                        st_id = int(input("Enter a student id: "))
                    except ValueError as e:
                        print(f"Value Error: {e}")
                    else:
                        break
                student = school.find_by_id(st_id)
                if student:
                    school.delete_student(st_id)
                    print(f"{student.name} has been deleted")
                else:
                    print("Student not found")
            case 6:
                school.rank_students()
            case 7:
                file_name = input("enter the file name you want to save data on: ")
                school.save_to_file(file_name=file_name)
            case 8:
                file_name = input("enter the file name you want to load data from: ")
                school.load_from_file(file_name=file_name)
            case 9:
                print("Logging Out...")
                is_running = False


    
if __name__ == '__main__':
    main()  
