from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Test1")
        self.student_with_courses = Student("Test2", {"math": ["x + y = z"]})

    def test_init(self):
        self.assertEqual("Test1", self.student)
        self.assertEqual("Test2", self.student_with_courses)


if __name__ == '__main__':
    main()
