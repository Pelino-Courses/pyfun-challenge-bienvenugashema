from student import Student
from instructor import Instructor
from course import Course
from enrollment import Enrollment
from teaching_assistant import TeachingAssistant

def display_menu():
    """Display the main menu options"""
    return """
    === University Management System ===
    
    1. Add New Instructor
    2. Create New Course
    3. Register Student
    4. Enroll Student in Course
    5. Add Teaching Assistant
    6. Display All Enrollments
    7. Exit
    
    Please select an option (1-7): """

def university_demo():
    print("Welcome to the University Management System!")
    
    # Initialize storage
    enrollments = Enrollment()
    instructors = {}
    courses = {}
    students = {}
    teaching_assistants = {}

    while True:
        try:
            choice = input(display_menu())
            
            if choice == "1":
                instructor_name = input("Enter the instructor's name: ")
                course_to_teach = input("Enter course to teach:")
                instructor = Instructor(instructor_name)
                instructors[instructor_name] = instructor
                instructor.display_instructor_info()
                courses[instructor.course] = course 
                print(instructor.display_instructor_info())

            elif choice == "2":
                course_name = input("Enter the course name: ")
                course = Course()
                courses[course_name] = course
                print(f"Course '{course_name}' has been created.")

            elif choice == "3":
                student_name = input("Enter the student's name: ")
                course_name = input("Enter the course to register for: ")
                if course_name not in courses:
                    print("Error: Course does not exist!")
                    continue
                student = Student(student_name, course_name)
                students[student_name] = student
                student.register_students()
                print(student.display_student_info())

            elif choice == "4":
                student_name = input("Enter student name to enroll: ")
                course_name = input("Enter course name: ")
                if student_name not in students or course_name not in courses:
                    print("Error: Student or course not found!")
                    continue
                print(enrollments.enroll_student(student_name, course_name))

            elif choice == "5":
                ta_name = input("Enter the teaching assistant's name: ")
                course_name = input("Enter the course to assist: ")
                if course_name not in courses:
                    print("Error: Course does not exist!")
                    continue
                ta = TeachingAssistant(ta_name, course_name)
                teaching_assistants[ta_name] = ta
                
                instructor_name = input("Enter instructor name to assist: ")
                if instructor_name in instructors:
                    print(ta.instructor_to_assist(instructor_name, course_name))
                    print(ta.student_to_teach(course_name, 95))
                    print(ta.display_info())
                else:
                    print("Error: Instructor not found!")

            elif choice == "6":
                print("\nCurrent Enrollments:")
                print(enrollments.display_enrollments())

            elif choice == "7":
                print("Thank you for using the University Management System!")
                break

            else:
                print("Invalid option! Please select a number between 1 and 7.")

        except ValueError as e:
            print(f"Error: Invalid input - {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        # Add a pause between operations
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    university_demo()
