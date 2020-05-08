# test code for students

# we want to see if our quicksort function works

from school_content import student, QuickSort 

# code 

newlist = [0, 9, 3, 7, 6, 1, 8, 2, 5, 4] # list to test our algorithm on 
n = len(newlist) 

qs = QuickSort() 

qs.quicksort(newlist, 0, n-1)   

print(newlist) 

# test with a student

