# a module with the information and functions about the students and assignments
'''
The school_content module has a 'student' class. The student has a full name, an email 
address, an ID number, and a list of grades. The students can be sorted by their names 
or their ID numbers; their grades can also be sorted from lowest to highest, in order to 
easily get each student's grade quartiles and average grade. 

We will sort the student's grades using a specialized sorting class; the algorithm 
used will be quicksort. 
'''     

class QuickSort:
    pass 


class student: 
    def __init__(self, name, student_id, email, grades=[]): 
        self.name = name
        self.student_id = student_id
        self.email = email
        self.grades = grades
    
    def add_grade(self): 
        # adds a grade to the 'grades' list
        total = float(input("Total Points Possible on Assignment: "))
        pts = float(input("Points Earned: ")) 
        letter_grade = pts / total
        self.grades.append(letter_grade) 

    def swap(self, n1, n2):
        # swaps assignments[n1] with assignments[n2]
        temp = self.grades[n1]
        self.grades[n1] = self.grades[n2]
        self.grades[n2] = temp 

    def partition(self, l, h):
        pass 

    def sort_grades(self, l, h):
        '''
        This function sorts the student's grades from lowest to highest. 
        Their grades are stored in the "grades" list. The algorithm used 
        will be quick sort, so we'll use the QuickSort class in the function.
        l: lowest index in array, h: highest index in array
        '''
        pass  

    # TODO: calculate grade quartiles and avg grade

    def get_grade_quartiles(self):
        # calculate grade quartiles
        pass

    def get_average(self):
        # get average grade
        pass 