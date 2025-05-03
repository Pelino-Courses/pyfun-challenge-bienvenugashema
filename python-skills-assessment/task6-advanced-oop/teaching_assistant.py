from student import Student
from instructor import Instructor

class TeachingAssistant(Student, Instructor):
    def __init__(self, name, course=None, grades=None):
        Student.__init__(self, name, course)
        Instructor.__init__(self, name)
        self.grades = grades
        pass
    def instructor_to_assist(self, name, course):
        self.course = course
        return f"Teaching assistant {self.name} is assisting instructor {name}"
    
    def student_to_teach(self, course, grade):
        self.course = course
        self.grades =grade

        return f"Teaching assistant: {self.name} is teaching the course {course} with grade {grade}"
    
    def display_info(self):
        return f"Teaching assistant name: {self.name} is teaching {self.course} with grade: {self.grades}"