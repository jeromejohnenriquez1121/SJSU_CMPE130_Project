# a module with the information and functions about the students and assignments
'''
The school_content module has a 'student' class. The student has a full name, an email 
address, an ID number, and a list of grades. The students can be sorted by their names 
or their ID numbers; their grades can also be sorted from lowest to highest, in order to 
easily get each student's grade quartiles and average grade. 

We will sort each student's grades with the quick sort algorithm; the specialized QuickSort() 
class will take in any array of numbers and sort them. The sort_grades() function in our
student class will make use of this function.
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
        print("--------------") 
        total = float(input("Total Points Possible on Assignment: "))
        pts = float(input("Points Earned: ")) 
        letter_grade = pts / total 
        self.grades.append(letter_grade) 

    # TODO: selection sort 
    # calls selection_sort function from SelectionSort class
    def sort_grades(self):
        n = len(self.grades) 
        # QuickSort().quicksort(self.grades, 0, n) 
 
    # TODO: calculate grade quartiles and avg grade

    def get_grade_quartiles(self):
        # calculate grade quartiles
        pass

    def get_average(self):
        # get average grade
        avg = 0
        # first, multiply each grade by its weight
        # next, add up the numbers
        wt = float(input("Grade Weight (e.g. for 20% weight, type 0.2): "))
        for grade in self.grades:
            grade *= wt
            avg += grade 
        return avg  





