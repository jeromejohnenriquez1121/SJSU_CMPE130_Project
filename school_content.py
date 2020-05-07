# a module with the information and functions about the students and assignments
'''
The school_content module has both 'assignment' and 'student' classes. The former,
of course, represents an assignment; it has a title, a due date, a total amount of 
possible points, and the total amount of points earned. The grade is found by dividing
the points earned by the total points possible on the assignment and multiplying this by 100.
The latter represents a student; the student has a full name, an email address, an ID 
number, and a list of assignments. The students can be sorted in different ways, whether
it be by their names, their ID numbers, or their grades. 
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
    
    def print_assignment(self):
        print("Assignment: " + self.assignment_title)
        print("Due Date: " + self.due_date)
        print("Grade: " + self.grade) 

class student: 
    def __init__(self, name, student_id, email, assignments): 
        self.name = name
        self.student_id = student_id
        self.email = email
        self.assignments = assignments 

    def set_name(self, name):
        self.name = name
    
    def set_id(self, student_id):
        self.student_id = student_id
    
    def set_email(self, email):
        self.email = email

    def get_name(self):
        return self.name 
    
    def get_id(self):
        return self.student_id
    
    def get_email(self):
        return self.email 
    
    def add_assignment(self): 
        # adds an 'assignment' object to the 'assignments' list
        # the 'assignment' values are user-inputted
        t = input("Assignment Title: ")
        d = input("Assignment Deadline: ")
        total = input("Total Points Possible on Assignment: ")
        pts = input("Points Earned: ")
        new_assignment = assignment(t, d, total, pts) 
        self.assignments.append(new_assignment) 


    def sort_by_grades(self):
        # sorts the students by their grades
        # the algorithm used is quick sort
        pass 