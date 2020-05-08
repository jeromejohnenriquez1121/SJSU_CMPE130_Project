from school_content import *
from hashing_function import *
import numpy as np

S = StudentHashTable()

while(1):

    print("Select one of the options from below:\n Enter the option number to perform that action. \n")
    print("1. Add a Student\n")
    print("2. Search for a Student\n")
    print("Enter <E> to exit the program")
    option = input()

    if option == "1":
        S.insertStudent()

    elif option == "2":
        while (1):
            sID = input('Provide Student ID: ')
            if len(sID) == 9:
                break
            else:
                print("Invalid Student ID entered. Please try again.")

        S.getStudentInfo(sID)

    else:
        print("Program exited")
        break

