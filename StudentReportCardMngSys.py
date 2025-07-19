#
import json
import csv
import os


class Student:

    student_id = 0

    def __init__(self,name,year):
        self.name = name
        self.year = year
        self.courses = {}
        Student.student_id += 1
        self.id = Student.student_id

    def __str__(self):
        return f"{self.name} (ID: {self.id}, Year: {self.year})"

    def __repr__(self):
        return self.__str__()

    def add_course(self,course_name,grade):
        self.courses[course_name] = grade

    def calculate_average(self):
        all_grades = 0
        num_courses = 0
        for course_name,grade in self.courses.items():
            all_grades += grade
            num_courses += 1
        if num_courses == 0:
            return 0
        else:
            return all_grades / num_courses
    
    def get_report(self):
        report = (f"=== Report for Student ID: {self.id}\n")
        report += (f"Name: {self.name}\n")
        report += (f"Year: {self.year}\n")

        report += ("Courses:\n")
        for course_name,grade in self.courses.items():
            report += (f"\t-{course_name}: {grade}\n")

        avg_grade = self.calculate_average()
        report += (f"Average Grade: {avg_grade}\n")

        report += ("=" * 10 + "\n")
        return report   

class School:
    def __init__(self):
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def find_by_id(self,id):
        for student in self.students:
            if student.id == id:
                return student
            
    def find_by_name(self,name):
        for student in self.students:
            if student.name.strip().lower() == name.strip().lower():
                return student
            
    def delete_student(self,id):
        for student in self.students:
            if student.id == id:
                self.students.remove(student)

    def display_all(self):
        if self.students:
            for student in self.students:
                print(f"{student.id} - {student.name} ({student.year})")
        else:
            print("No Students found in school")
            
    def rank_students(self):
        ranking = []

        for student in self.students:
            avg = student.calculate_average()
            ranking.append((avg, student.name))  # tuple of (avg, name)

        ranking.sort(reverse=True)  

        for i, (avg, name) in enumerate(ranking, start=1):
            print(f"{i}. {name}: {avg:.2f}")

    def save_to_file(self,file_name):
        data = []
        for student in self.students:
                    data.append({
                        "id": student.id,
                        "name": student.name,
                        "year": student.year,
                        "courses": student.courses,
                        "average": student.calculate_average()
                    })
        with open(file_name,"w") as file:
            if "txt" in file_name:
                for info in self.students:
                    for cname,grade in info.courses.items():
                        txt_data = f"id: {info.id}\nname: {info.name}\nyear: {info.year}\n{cname}: {grade}\nAverage: {info.calculate_average()}\n"
                        file.write(txt_data)
                print(f"Saved in txt file: {file_name}")
            elif "json" in file_name:
                json.dump(data,file,indent=4)
                print(f"Saved in json file: {file_name}!")
            elif "csv" in file_name:
                writer= csv.writer(file)
                writer.writerow(["ID", "Name", "Year", "Course", "Grade"])
                for student in self.students:
                    for course, grade in student.courses.items():
                        writer.writerow([student.id, student.name, student.year, course, grade])
                print(f"Saved in csv file: {file_name}")

    def load_from_file(self,file_name):
        if not os.path.exists(file_name):
            print("File not found !")
            return

        with open(file_name,"r") as file:
            if "txt" in file_name:
                content = file.read()
                print(content)
                print("Loading Done !")
            elif "json" in file_name:
                try:
                    data = json.load(file)

                    self.students = []  
                    Student.student_id = 0  

                    for item in data:
                        student = Student(item["name"], item["year"])
                        student.courses = item["courses"]
                        Student.student_id = max(Student.student_id, item["id"]) 
                        student.id = item["id"]
                        self.students.append(student)
                    print("Loading Done !")

                except json.JSONDecodeError:
                    print("Invalid JSON file format")

            elif "csv" in file_name:
                content = csv.reader(file)
                for data in content:
                    print(data)
                print("Loading Done !")

