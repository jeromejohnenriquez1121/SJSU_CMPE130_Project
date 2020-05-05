# a module with the information and functions about the students and assignments

class assignment:
    def __init__(self, due_date, grade):
        self.due_date = due_date
        self.grade = grade

class student: 
    def __init__(self, name, student_id, email, assignments):
        self.name = name
        self.student_id = student_id
        self.email = email
        self.assignments = assignments 