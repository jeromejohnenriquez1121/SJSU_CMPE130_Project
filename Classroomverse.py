from tkinter import *
from _ast import Lambda

def main():
    root = Tk()
    root.title('Classroomverse')
    root.geometry('853x480')
    root.configure(bg='white')

    def Main_shows_people():
        random = Label(main, text="These are people.")
        random.pack()

    #def Main_shows_assignments():

    #def Main_shows_grades():

    title = Label(root, text="Classroomverse", font=("Tahoma", 26), bg="white", padx=3, pady=3)
    title.pack(side="top")
    sidebar = Frame(root, width=200, bg='#CCF7FF', borderwidth=1)
    sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

    button1 = Button(sidebar, text="Home", padx=10, pady=10, command=Main_shows_people, relief=GROOVE, bg='#CCF7FF')
    button2 = Button(sidebar, text="Assignments", padx=10, pady=10, command=Main_shows_people, relief=GROOVE, bg='#CCF7FF')
    button3 = Button(sidebar, text="Grades", padx=10, pady=10, command=Main_shows_people, relief=GROOVE, bg='#CCF7FF')
    button4 = Button(sidebar, text="People", padx=10, pady=10, command=Main_shows_people, relief=GROOVE, bg='#CCF7FF')
    button1.pack(fill=X)
    button2.pack(fill=X)
    button3.pack(fill=X)
    button4.pack(fill=X)
    main = Frame(root, bg='gray', width=500,)
    main.pack(expand=True, fill='both', side='right')
    root.mainloop()

if __name__=='__main__':
    main()