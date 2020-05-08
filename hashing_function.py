from school_content import *
import numpy as np


def make_student():
    newStudent = {}
    print("Enter the student info as per each instruction:\n")
    newStudent['name'] = input('Please enter Student Name: ')
    while(1):
        newStudent['student_id'] = input('Please enter Student ID: ')
        if len(newStudent['student_id']) == 9:
            break
        else:
            print("Invalid Student ID entered. Please try again.")

    newStudent['email'] = input('Please give Student Email: ')

    print("\n Student", newStudent['name'], "created.")
    s = student(newStudent['name'], newStudent['student_id'], newStudent['email'], " ")
    return s


class StudentHashTable:
    def __init__(self):
        self.studentList = ["NULL"]*100

    def insertStudent(self):
        print("Inserting Student")
        newStudent = make_student()
        sID = newStudent.student_id
        indexNumber = int(sID[6:9]) % len(self.studentList)

        for e in self.studentList:
            if e != "NULL" and e.email == newStudent.email:
                print("Student with the same email already exist. Please Try again")
                return

        if self.studentList[indexNumber] == "NULL":
            self.studentList[indexNumber] = newStudent
            print(newStudent.name, "added to the table.")
        else:
            while(1):
                if self.studentList[indexNumber].student_id == newStudent.student_id or \
                        self.studentList[indexNumber].email == newStudent.email:
                    print("Student with this ID or Email is already added! Cannot make duplicate entry.\n\n")
                    break
                elif self.studentList[indexNumber] == "NULL":
                    self.studentList[indexNumber] = student
                    print(newStudent.name, "added to the table\n\n")
                    break
                indexNumber = (indexNumber + 1) % len(self.studentList)

    def getStudentInfo(self, sID):
        indexNumber = int(sID[6:8]) % len(self.studentList)

        if self.studentList[indexNumber].student_id == sID:
            print(self.studentList[indexNumber])
            return
        else:
            while indexNumber != len(self.studentList) and self.studentList[indexNumber] != "NULL":
                if self.studentList[indexNumber].student_id == sID:
                    print(self.studentList[indexNumber])
                    return
                indexNumber = (indexNumber + 1) % len(self.studentList)
        print("Student with Student ID " + sID + " is not found\n\n")
        return














