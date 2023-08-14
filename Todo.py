from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To_Do_List')
        self.root.geometry('490x570')

        self.label = Label(self.root,text='To-Do-list-app',font='ariel, 25 bold',width=10,bd=5, bg='blue',fg='black')
        self.label.pack(side='top',fill=BOTH)

        self.label2 = Label(self.root, text='Add Task',font='ariel, 18 bold',width=10,bd=5, bg='blue',fg='black')
        self.label2.place(x=40,y=54)

        self.label3 = Label(self.root, text= 'Task',font='ariel, 18 bold',width=10,bd=5, bg='blue',fg='black')
        self.label3.place(x=320,y=54)
        
        self.main_text=Listbox(self.root,height=9,bd=5,width=23,font=("ariel",20,"italic","bold"))
        self.main_text.place(x=200,y=100)

    def main():
        root = Tk()
        ui = todo(root)
        root.mainloop()

    if __name__=="__main__":
        main()