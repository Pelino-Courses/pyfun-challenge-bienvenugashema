from person import Person
from student import Student
from instructor import Instructor
#acces student
inst = Instructor(" ")
class Course:
    def __init__(self):
        pass
        
    def display_course_info(self):
        inst.display_instructor_info()
        self.instructor = input("Teacher name: ")
        #calling course name from instructor
        return f"Teacher is:{self.instructor} teaches {inst.course}"
    
    
