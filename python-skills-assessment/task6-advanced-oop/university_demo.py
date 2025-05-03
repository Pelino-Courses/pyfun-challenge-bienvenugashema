from student import Student
from instructor import Instructor
from course import Course
from enrollment import Enrollment
from teaching_assistant import TeachingAssistant

def university_demo():
    print("Welcome to the University Management System!")

    # Create an instructor
    instructor_name = input("Enter the instructor's name: ")
    instructor = Instructor(instructor_name)
    print(instructor.display_instructor_info())

    # Create a course
    course_name = input("Enter the course name: ")
    course = Course()
    print(f"Course '{course_name}' has been created.")

    # Register a student
    student_name = input("Enter the student's name: ")
    student = Student(student_name, course_name)
    student.register_students()
    print(student.display_student_info())

    # Enroll the student in the course
    enrollment = Enrollment()
    print(enrollment.enroll_student(student_name, course_name, instructor_name))

    # Display all enrollments
    print("\nCurrent Enrollments:")
    print(enrollment.display_enrollments())

    # Create a teaching assistant
    ta_name = input("Enter the teaching assistant's name: ")
    ta = TeachingAssistant(ta_name, course_name)
    print(ta.instructor_to_assist(instructor_name, course_name))
    print(ta.student_to_teach(course_name, 95))
    print(ta.display_info())

if __name__ == "__main__":
    university_demo()
