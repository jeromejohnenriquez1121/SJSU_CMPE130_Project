# a module with the information and functions about the students and assignments
'''
The school_content module has both 'assignment' and 'student' classes. The former,
of course, represents an assignment; it has a title, a due date, a total amount of 
possible points, and the total amount of points earned. The grade is found by dividing
the points earned by the total points possible on the assignment and multiplying this by 100.
The latter represents a student; the student has a full name, an email address, an ID 
number, and a list of assignments. The students can be sorted by their names or their 
ID numbers; their grades can also be sorted from lowest to highest, in order to easily
get each student's grade quartiles and average grade. 

We will sort the student's assignments by grade using the sort_grades() function; the algorithm 
used will be quicksort. We need a swap() function and an overloaded less-than operator to do this. 
The less-than operator will be in the 'assignment' class; the swap() function will be in the 
'student' class.
'''
class assignment:
    def __init__(self, assignment_title, due_date, total_points, points_earned):
        self.assignment_title = assignment_title
        self.due_date = due_date
        self.total_points = total_points
        self.points_earned = points_earned
        self.grade = (points_earned/total_points) * 100
    
    def get_grade(self):
        return self.grade 

    def __lt__(self, new_assignment):
        # tests if the current assignment has a lower grade
        # than new_assignment
        if (self.grade < new_assignment.grade):
            return True
        else:
            return False 
    
    def print_assignment(self):
        print("Assignment: " + self.assignment_title)
        print("Due Date: " + self.due_date)
        print("Grade: " + self.grade) 

class student: 
    def __init__(self, name, student_id, email, assignments=[]): 
        self.name = name
        self.student_id = student_id
        self.email = email
        self.assignments = assignments 
    
    def add_assignment(self): 
        # adds an 'assignment' object to the 'assignments' list
        # the 'assignment' values are user-inputted
        t = input("Assignment Title: ")
        d = input("Assignment Deadline: ")
        total = float(input("Total Points Possible on Assignment: "))
        pts = float(input("Points Earned: ")) 
        new_assignment = assignment(t, d, total, pts) 
        self.assignments.append(new_assignment) 

    def swap(self, n1, n2):
        # swaps assignments[n1] with assignments[n2]
        temp = self.assignments[n1]
        self.assignments[n1] = self.assignments[n2]
        self.assignments[n2] = self.assignments[n1] 
        
    def partition(self, l, h):
        pivot = self.assignments[h-1]
        i = l - 1
        for j in range(l, h):
            if (self.assignments[j] < pivot):
                i += 1
                self.swap(i, j) # swaps self.assignments[i] with self.assignments[j]  

        self.swap(self.assignments[i+1], self.assignments[h]) 
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
