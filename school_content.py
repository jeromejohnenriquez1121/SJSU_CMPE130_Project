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

def get_median_index(array):
    # like get_median, but it returns median index
    list_length = len(array) 
    if (list_length % 2 == 0): # for even # of elements
        mid1 = int(list_length - 1 / 2)
        mid2 = int(list_length / 2) 
        return [mid1, mid2] 
    else: # for odd # of elements 
        mid = list_length // 2
        return [mid] 


class QuickSort: 
    # only two functions needed: partition and quicksort
    # 'collection': the array to be sorted
    def partition(self, collection, lo, hi):
        # hi = len(collection) - 1
        j = lo # collection[j] and everything behind it must be less than pivot
        pivot = hi # selecting last item as pivot
        # what do we know? We know that we must go from lo to hi, until we find an item less than the pivot
        # we use i and j for this, i is in the for loop, j is the index for most recent element < pivot element
        for i in range(lo, hi):
            # when collection[i] < collection[pivot], we've found a left partition item
            # we swap collections[i] and collections[j], so now j is the first element < pivot   
            # we increment j to move on to find the next element < pivot        
            if (collection[i] < collection[pivot]): 
                collection[i], collection[j] = collection[j], collection[i]
                j += 1
        # now we swap our 'marker' j with the pivot
        collection[pivot], collection[j] = collection[j], collection[pivot] 
        return j 


    def quicksort(self, collection, lo, hi):
        # hi = len(collection) - 1
        if (lo < hi):
            pivot = self.partition(collection, lo, hi)
            self.quicksort(collection, lo, pivot-1)
            self.quicksort(collection, pivot+1, hi) 


class student: 
    def __init__(self, name, student_id, email, grades=[], avg=0, quartiles=[]): 
        self.name = name
        self.student_id = student_id
        self.email = email
        self.grades = grades
        self.avg = avg
        self.quartiles = quartiles 
    
    def add_grade(self): 
        # adds a grade to the 'grades' list
        print("--------------") 
        total = float(input("Total Points Possible on Assignment: "))
        pts = float(input("Points Earned: ")) 
        letter_grade = (pts / total) * 100 
        self.grades.append(letter_grade) 

    # calls quicksort function from QuickSort class
    def sort_grades(self):
        n = len(self.grades) 
        QuickSort().quicksort(self.grades, 0, n-1)   

    def calculate_grade_quartiles(self):
        # calculate grade quartiles with global median function
        # Q1 (lower quartile): median of lower half
        # Q2: median
        # Q3 (upper quartile): median of upper half 
        q1 = 0
        q2 = 0
        q3 = 0 
        n1 = len(self.grades) 
        # 1. make sure array is sorted in ascending order
        self.sort_grades() 
        # 2. find median of array to divide it in lower and upper half
        index_mid = get_median_index(self.grades) # the middle index/indices, in list form!
        # getting Q1 and Q3 will be different depending on whether or not
        # array length is odd or even
        # even: lower half is from 0 to index before first of the two middle numbers, 
        # upper half is from that index to end
        # odd: lower half is from 0 to median index, upper half is from median index to end
        # either way, lower half and upper half are split between index_mid[0]
        mid = index_mid[0]
        
        lower_half = 

    def get_quartiles(self):
        return self.quartiles 
        


    def calculate_average(self):
        # get average grade
        avg_grade = 0
        # we must divide sum of weighted grades by sum of weights
        grade_sum = 0
        wt_sum = 0 
        # first, multiply each grade by its weight
        # next, add up the numbers
        for grade in self.grades:
            wt = float(input(f"Grade Weight (e.g. for 20% weight, type 0.2) for {grade}: ")) 
            grade *= wt
            grade_sum += grade # remember, grade_sum: sum of WEIGHTED grades
            wt_sum += wt  
        # finally, do the division and store result in 'avg' variable
        avg_grade = grade_sum / wt_sum 
        self.avg = avg_grade 
    
    def get_average(self):
        return self.avg  

    def student_status(self):
        # compares average grade with passing grade
        # any grade below passing - 'need to improve'
        # 70-79: 'ok, but could be better'
        # 80-89: 'ok/good'
        # 90-99: 'excellent/amazing' 
        passing = 70.00     
        temp_name = self.name
        if (self.avg < passing):
            print(f"{temp_name} has a low grade in the class and needs to improve. They should do the assignments and try to get high scores on the exams to raise their grade")
        elif (self.avg >= passing and self.avg <= 79):
            print(f"{temp_name} is passing the class, but could be doing much better. They should keep up with the assignments and study hard for the exams.")
        elif (self.avg >= 80 and self.avg <= 89):
            print(f"{temp_name} has a good grade in the class and can bump it up to an A if they do well in the exams.")
        else:
            print(f"{temp_name}'s grade is excellent! To keep it up, they should still try and do well on the exams.") 

