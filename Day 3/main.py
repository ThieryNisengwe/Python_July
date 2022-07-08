
from platform import python_branch


class Student:
    # Constructor
    def __init__(self, first_name, last_name, age, instructor, course):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.instructor = instructor
        self.course = course

    def print_info(self, message):
        print(message)
        print(f"Name:{self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Instructor: {self.instructor}")
        print(f"CourseL {self.course}")


class Course:
    def __init__(self, data):
        self.name = data["name"]
        self.instructor = data["instructors"]
        self.program = data["program"]

    def print_instructor_list(self):
        for instructor in self.instructor:
            print(instructor)
            return self

    def update_instructor(self, new_name, index):
        if index < len(self.instructor):
            self.instructor[index] = new_name
            return self

    def print_info(self):
        print(f"Program: {self.program}")
        print(f"Name: {self.name}")
        self.print_instructor_list()
        return self


python = {
    "name": "Python/Flask",
    "instructors": ["Alfredo Salazar", "Spencer Rauch", "Tyler Tybault"],
    "program": "Full stack"
}
course_python = Course(python)

course_python.update_instructor("Ryan Mendez", 2)
course_python.print_info()


student_alex = Student("Alex", "Miller", 20, "Nichole", "Web Fundamentals")
student_martha = Student("Martha", "Smith", 25, "Alfredo", "Python")
print(student_alex)

print(student_alex.first_name, student_alex.last_name, student_alex.age)

student_alex.print_info("Hey there!")

student_martha.print_info("Howdy!")
