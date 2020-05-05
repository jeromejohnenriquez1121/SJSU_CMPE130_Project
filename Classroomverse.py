from tkinter import *
from school_content import * 


def main():
    root = Tk()
    root.title('Classroomverse')
    root.geometry('853x480')
    root.configure(bg='white')

    def show_home_page():
        HomeLabel = Label(main, text="This is the homepage.")
        HomeLabel.pack()

    def show_people():
        PeopleLabel = Label(main, text="These are people.")
        PeopleLabel.pack()

    def shows_assignments():
        AssignmentsLabel = Label(main, text="These are assignments.")
        AssignmentsLabel.pack()
    def shows_grades():
        GradesLabel = Label(main, text="These are grades.")
        GradesLabel.pack()

    title = Label(root, text="Classroomverse", font=("Tahoma", 26), bg="white", padx=3, pady=3)
    title.pack(side="top")
    sidebar = Frame(root, width=200, bg='#CCF7FF', borderwidth=1)
    sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

    button1 = Button(sidebar, text="Home", padx=10, pady=10, command=show_home_page, relief=GROOVE, bg='#CCF7FF')
    button2 = Button(sidebar, text="Assignments", padx=10, pady=10, command=shows_assignments, relief=GROOVE, bg='#CCF7FF')
    button3 = Button(sidebar, text="Grades", padx=10, pady=10, command=shows_grades, relief=GROOVE, bg='#CCF7FF')
    button4 = Button(sidebar, text="People", padx=10, pady=10, command=show_people, relief=GROOVE, bg='#CCF7FF')
    button1.pack(fill=X)
    button2.pack(fill=X)
    button3.pack(fill=X)
    button4.pack(fill=X)
    main = Frame(root, bg='gray', width=500,)
    main.pack(expand=True, fill='both', side='right')
    root.mainloop()

if __name__=='__main__':
    main()