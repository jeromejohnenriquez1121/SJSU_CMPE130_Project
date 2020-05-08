# a module with the information and functions about the students and assignments
'''
The school_content module has a 'student' class. The student has a full name, an email 
address, an ID number, and a list of grades. The students can be sorted by their names 
or their ID numbers; their grades can also be sorted from lowest to highest, in order to 
easily get each student's grade quartiles and average grade. 

We will sort the student's grades using the sort_grades() function; the algorithm 
used will be quicksort. We need a swap() function and an overloaded less-than operator to do this. 
The less-than operator will be in the 'assignment' class; the swap() function will be in the 
'student' class.
'''     

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
        pivot = self.grades[h-1] 
        i = l - 1
        for j in range(l, h):
            if (self.grades[j] < pivot): 
                i += 1
                self.swap(i, j) 
        self.swap(i+1, h)   
        return i + 1

    def sort_grades(self, l, h):
        '''
        This function sorts the student's grades from lowest to highest. 
        Their grades are stored in the "assignments" list; each "assignment" 
        object has a grade. The algorithm used will be quick sort.
        l: lowest index in array, h: highest index in array
        '''
        if l < h:
            pivot = self.partition(l, h-1)
            self.sort_grades(l, pivot - 1) 
            self.sort_grades(pivot + 1, h-1)  

    # TODO: calculate grade quartiles and avg grade