from StudentReportCardMngSys import Student, School
import unittest

class TestStudent(unittest.TestCase):
    def test_add_course_and_average(self):
        s = Student("Saad", 2)
        s.add_course("Math", 90)
        s.add_course("Science", 80)
        self.assertEqual(s.calculate_average(), 85)

    def test_get_report(self):
        s = Student("Saad", 2)
        s.add_course("Math", 90)
        s.add_course("Science", 80)
        report = s.get_report()
        self.assertIn("Saad", report)
        self.assertIn("Math", report)
        self.assertIn("Science", report)

class TestSchool(unittest.TestCase):
    def test_add_and_find_student(self):
        school = School()
        s = Student("Saad", 2)
        school.add_student(s)
        found = school.find_by_name("Saad")
        self.assertEqual(found.name, "Saad")

    def test_find_by_id(self):
        school = School()
        s = Student("Ali", 3)
        school.add_student(s)
        found = school.find_by_id(s.id)
        self.assertEqual(found.name, "Ali")

    def test_json_save_load(self):
        school = School()
        s = Student("TestUser", 10)
        s.add_course("Math", 100)
        school.add_student(s)
        school.save_to_file("test_data.json")

        school2 = School()
        school2.load_from_file("test_data.json")
        self.assertEqual(school2.students[0].name, "TestUser")


if __name__ == '__main__':
    unittest.main()
