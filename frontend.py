from tkinter import *
import backend

#--------------------------------------------------------------
def view_command():
    list_view.delete(0,END)
    for row in backend.view_all():
        list_view.insert(END,row)
def search_command():
    list_view.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list_view.insert(END,row) #to insert unto the list
def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list_view.delete(0, END) #to make sure that the list is empty
    list_view.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
def get_selected_row(event):
    global selected_tuple
    index=list_view.curselection()[0]
    selected_tuple=list_view.get(index)
    title.delete(0,END)
    title.insert(END,selected_tuple[1])
    author.delete(0,END)
    author.insert(END,selected_tuple[2])
    year.delete(0,END)
    year.insert(END,selected_tuple[3])
    isbn.delete(0,END)
    isbn.insert(END,selected_tuple[4])

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

def close_command():
    window.destroy()
#--------------------------------------------------------------
window=Tk()
window.wm_title("BookStore")

title = Label(window,text="Title")
title.grid(row=0,column=0)

year = Label(window,text="Year")
year.grid(row=1,column=0)

author = Label(window,text="Author")
author.grid(row=0,column=2)

isbn = Label(window,text="ISBN")
isbn.grid(row=1,column=2)

#------------------------------------------------------------

title_text=StringVar()
title=Entry(window,textvariable=title_text)
title.grid(row=0,column=1)

year_text=StringVar()
year=Entry(window,textvariable=year_text)
year.grid(row=1,column=1)

author_text=StringVar()
author=Entry(window,textvariable=author_text)
author.grid(row=0,column=3)

isbn_text=StringVar()
isbn=Entry(window,textvariable=isbn_text)
isbn.grid(row=1,column=3)

#-----------------------------------------------------------

list_view=Listbox(window,height=10,width=40)
list_view.grid(row=2,column=0,rowspan=6,columnspan=2)

scroll=Scrollbar(window)
scroll.grid(row=2,column=2,rowspan=6)

list_view.configure(yscrollcommand=scroll.set) #yscrollcommand is used for y axis scolling
scroll.configure(command=list_view.yview) #yview means the scrollbar changes the yview of the listbox

list_view.bind("<<ListboxSelect>>",get_selected_row)

#--------------------------------------------------------------

view=Button(window,text="view_all",width=12,command=view_command)
view.grid(row=2,column=3)

search=Button(window,text="search_entry",width=12,command=search_command)
search.grid(row=3,column=3)

add=Button(window,text="add_entry",width=12,command=add_command)
add.grid(row=4,column=3)

update=Button(window,text="update_entry",width=12,command=update_command)
update.grid(row=5,column=3)

delete=Button(window,text="delete",width=12,command=delete_command)
delete.grid(row=6,column=3)

close=Button(window,text="close",width=12,command=close_command)
close.grid(row=7,column=3)

#-------------------------------------------------------------

window.mainloop()