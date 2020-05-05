# a module with the information and functions about the students and assignments

class assignment:
    def __init__(self, assignment_title, due_date, total_points, points_earned):
        self.assignment_title = assignment_title
        self.due_date = due_date
        self.total_points = total_points
        self.points_earned = points_earned
        self.grade = (points_earned/total_points) 

class student: 
    def __init__(self, name, student_id, email, assignments): 
        self.name = name
        self.student_id = student_id
        self.email = email
        self.assignments = assignments 
    
    def add_assignment(self): 
        # adds an 'assignment' object to the 'assignments' list
        # the 'assignment' values are user-inputted
        t = input("Assignment Title: ")
        d = input("Assignment Deadline: ")
        total = input("Total Points Possible on Assignment: ")
        pts = input("Points Earned: ")
        new_assignment = assignment(t, d, total, pts) 
        self.assignments.append(new_assignment) 

