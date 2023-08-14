from tkinter import *
from tkinter.font import Font

#instantiate tkinter window
root=Tk()
root.title('To Do List')
root.geometry("500x500")
root.resizable(False,False)

#define personal font
my_font= Font(family="Calibri",size=15,weight="bold")

#create new frame within the window
my_frame = Frame(root)
my_frame.pack(pady=10)

#create a new listbox
my_list= Listbox(my_frame, font=my_font, width=45,height=10,bd=2,bg="SystemButtonFace",fg="#464646")
my_list.pack(side=LEFT,fill=BOTH)

#create and add scroll bar to listbox
my_scroll=Scrollbar(my_frame)
my_scroll.pack(side=RIGHT,fill=BOTH)
my_list.config(yscrollcommand=my_scroll.set)
my_scroll.config(command=my_list.yview)

#create an input or enter placeholder
my_entry= Entry(root, font=("Calibri",20))
my_entry.pack(pady=10)

#create buttons
button_frame= Frame(root)
button_frame.pack(pady=20)

#method to add a value to the list
def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

#method to delete a value from the list
def delete_item():
    my_list.delete(ANCHOR)

#set button properties
add_button= Button(button_frame, text="Add Item", command=add_item)
delete_button= Button(button_frame, text="Delete Item", command=delete_item)

add_button.grid(row=0, column=0, padx=20)
delete_button.grid(row=0, column=1, padx=20)


root.mainloop()
#end
