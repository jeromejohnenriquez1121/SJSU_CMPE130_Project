
from tkinter import *
from school_content import QuickSort, student
from hashing_function import StudentHashTable
import NumPy as np


def main():
    print("Welcome to Classroomverse")
    studentList = StudentHashTable()
    option = 0
    while option != 8:
        option = int(input('1. Add student information: \n'
                           '2. Display student information: \n'
                           '3. Get Quartiles\n'
                           '4. Display and Sort Grades\n'
                           '5. Quit\n'
                           'Enter option: '))
        if option == 1:
            studentList.insertStudent()

        elif option == 2:
            id = int(input("Enter ID: "))
            temp = studentList.getStudent(id)
            temp.student_status()

        elif option == 3:
            id = int(input("Enter ID: "))
            temp = studentList.getStudent(id)
            temp.calculate_grade_quartiles()
        elif option == 4:
            id = int(input("Enter ID: "))
            temp = studentList.getStudent(id)
            temp.student_status()
        else:
            print("Please enter a number that follows one of the options.")
