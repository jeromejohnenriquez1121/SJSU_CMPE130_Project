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
    # only two functions needed: partition and quicksort
    # 'collection': the array to be sorted
    def partition(self, collection, lo, hi):
        # hi = len(collection) - 1
        j = self.lo # collection[j] and everything behind it must be less than pivot
        pivot = self.hi # selecting last item as pivot
        # what do we know? We know that we must go from lo to hi, until we find an item less than the pivot
        # we use i and j for this, i is in the for loop, j is the index for most recent element < pivot element
        for i in range(lo, hi):
            if (self.collection[i] < self.collection[j]):
                
        # when collection[i] < collection[pivot], we've found a left partition item
        # we swap collections[i] and collections[j], so now j is the first element < pivot
        # after the for-loop, pivot should be in its correct position
        # all items to its left must be less than it, al items to its right must be greater than it


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





