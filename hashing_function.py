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
    s = student(newStudent['name'], newStudent['student_id'], newStudent['email'], grades=[], avg=0, quartiles=[], completed = False)
    return s


class StudentHashTable:

    def __str__(self):
        ret = ""
        for s in self.studentList:
            if s!= "NULL":
                ret += str(s) + "-x-x-x-x-x-x-x-x-x-x-x-x-x-x\n"
        return ret

    def __init__(self):
        self.studentList = ["NULL"]*100

    def insertStudent(self):
        print("Inserting Student")
        newStudent = make_student()
        sID = newStudent.student_id
        sEmail = newStudent.email
        indexNumber = int(sID[7:9]) % len(self.studentList)

        if self.studentList[indexNumber] == "NULL":
            self.studentList[indexNumber] = newStudent
            print(newStudent.name, "added to the table at index",indexNumber,"\n\n")
            return

        elif self.studentList[indexNumber] != "NULL":
            while True:
                if self.studentList[indexNumber] == "NULL":
                    self.studentList[indexNumber] = newStudent
                    print(newStudent.name, "added to the table at index", indexNumber,"\n\n")
                    return
                elif self.studentList[indexNumber].student_id == sID:
                    print("Student is already added! Cannot make duplicate entry.\n\n")
                    return
                indexNumber = (indexNumber + 1) % len(self.studentList)

    def getStudentInfo(self, sID):
        indexNumber = int(sID[7:9]) % len(self.studentList)

        if self.studentList[indexNumber].student_id == sID:
            print(self.studentList[indexNumber])
            return
        else:
            while self.studentList[indexNumber] != "NULL":
                if self.studentList[indexNumber].student_id == sID:
                    print(self.studentList[indexNumber])
                    return
                indexNumber = (indexNumber + 1) % len(self.studentList)
        print("Student with Student ID [" + sID + "] is not found\n\n")
        return

    def getStudent(self,sID):
        indexNumber = int(sID[7:9]) % len(self.studentList)

        if self.studentList[indexNumber].student_id == sID:
            return self.studentList[indexNumber]
        else:
            while self.studentList[indexNumber] != "NULL":
                if self.studentList[indexNumber].student_id == sID:
                    return self.studentList[indexNumber]
                indexNumber = (indexNumber + 1) % len(self.studentList)
        print("Student with Student ID [" + sID + "] is not found\n\n")
        return