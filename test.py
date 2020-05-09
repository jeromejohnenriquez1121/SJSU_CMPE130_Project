# test code for students

# we want to see if our quicksort function works

from school_content import student, QuickSort 

# code 

'''
newlist = [0, 9, 3, 7, 6, 1, 8, 2, 5, 4] # list to test our algorithm on 
n = len(newlist) 

qs = QuickSort() 

qs.quicksort(newlist, 0, n-1)   

print(newlist) 
'''

# test with a student

saima = student("Saima", "012257752", "saima.yunus@sjsu.edu")
n1 = int(input("# OF ASSIGNMENTS: "))

for i in range(n1):
    saima.add_grade() 

# first test: sort grades
saima.sort_grades()
print(saima.grades) 

# second test: get weighted avg
saima.calculate_average()
avg = saima.get_average() 
print(f"Average: {avg}") 

# third test: show if student is doing well or not

# fourth test: get quartiles
saima.calculate_grade_quartiles() 
q1_to_q3 = saima.get_quartiles()
print(q1_to_q3) 