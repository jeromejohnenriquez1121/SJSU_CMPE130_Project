from school_content import *
from hashing_function import *
import numpy as np

S = StudentHashTable()

while True:

    print("Select one of the options from below:\n Enter the option number to perform that action. \n")
    print("[1]. Add a Student\n")
    print("[2]. Search for a Student\n")
    print("[3]. Add grades for a student\n")
    print("[4]. Make grade calculations for a student\n")
    print("[5]. Print the Student List\n")
    print("[6]. To Exit the Program\n")

    option = input()

    if option == "1":
        S.insertStudent()

    elif option == "2":
        while True:
            sID = input('Provide Student ID: ')
            if len(sID) == 9:
                break
            else:
                print("Invalid Student ID entered. Please try again.")
        S.getStudentInfo(sID)

    elif option == "3":
        while True:
            sID = input('Provide Student ID: ')
            if len(sID) == 9:
                break
            else:
                print("Invalid Student ID entered. Please try again.")

        modify_student = S.getStudent(sID)

        while True:
            modify_student.add_grade()
            response = input("Press <R> to grade another assignment, press any key to finish")
            if response == "R":
                continue
            else:
                break

    elif option == "4":
        while True:
            sID = input('Provide Student ID: ')
            if len(sID) == 9:
                break
            else:
                print("Invalid Student ID entered. Please try again.")

        calc_student = S.getStudent(sID)

        calc_student.sort_grades()
        calc_student.calculate_grade_quartiles()
        calc_student.calculate_average()

    elif option == "5":
        print(S)

    elif option == "6":
        print("Program exited")
        break

    else:
        print("Choose the correct option. Please Try Again")
