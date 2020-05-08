from school_content import *

# test code for students

# we want to see if our quicksort function works

saima = student("Saima Yunus", "012257752", "saima.yunus@sjsu.edu") 


n2 = int(input("# OF ASSIGNMENTS: "))
for j in range(n2):
    saima.add_grade()
 

saima.sort_grades(0, n2) 

print(saima.grades) 


