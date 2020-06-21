
from tkinter import *
import backend

window = Tk()

window.wm_title("Homely Beds: Find the Perfect Accommodation")
window.iconbitmap(r'D:\book_store1\homely1.ico')

#labels
l1 = Label(window,text='Pg Name')
l2 = Label(window,text='Pitched by')
l3 = Label(window,text='Client Name')
l4 = Label(window,text='Amount')
l5 = Label(window,text='College')
l6= Label(window,text='Contact No')
l7 = Label(window,text='Date')
l8 = Label(window,text='Commission')
l1.grid(row=0,column=0)
l2.grid(row=0,column=2)
l3.grid(row=1,column=0)
l4.grid(row=1,column=2)
l5.grid(row=2,column=0)
l6.grid(row=0,column=4)
l7.grid(row=1,column=4)
l8.grid(row=2,column=2) # commmision

pg_name = StringVar()
pitched_by = StringVar()
client_name= StringVar()
amount = StringVar()
college=StringVar()
contact= StringVar()
date_t=StringVar()
commision = StringVar()
e1 = Entry(window,textvariable=pg_name)
e2 = Entry(window,textvariable=pitched_by)
e3 = Entry(window,textvariable=client_name)
e4 = Entry(window,textvariable=amount)
e5 = Entry(window,textvariable=college)
e6 = Entry(window,textvariable=contact)
e7 = Entry(window,textvariable=date_t)
e8 = Entry(window,textvariable=commision)

e1.grid(row=0,column=1)
e2.grid(row=0,column=3)
e3.grid(row=1,column=1)
e4.grid(row=1,column=3)
e5.grid(row=2,column=1)
e6.grid(row=0,column=5)
e7.grid(row=1,column=5)
e8.grid(row=2,column=3)

#listbox

lb1 = Listbox(window,height =8,width=80,bg="medium aquamarine",bd=5,)
lb1.grid(row=2,column=0,rowspan=10,columnspan=3)

#scrollbar
sb = Scrollbar(window)
#sb.pack(side=RIGHT,fill=Y)
sb.grid(row=2,column=3,rowspan = 6)

#binding list and scrollbar
lb1.configure(yscrollcommand=sb.set)
sb.configure(command=lb1.yview)

#all functions to call backend
def viewall():
    lb1.delete(0,END)
    for row in backend.view():
        lb1.insert(END,row)

def search_button():
    lb1.delete(0,END)
    for row in backend.search(client_name.get(),pg_name.get(),pitched_by.get(),amount.get(),college.get(),contact.get(),date_t.get(),commision.get()):
        lb1.insert(END,row)

def Add_entry():
    backend.insert(client_name.get(),pg_name.get(),pitched_by.get(),amount.get(),college.get(),contact.get(),date_t.get(),commision.get())
    lb1.delete(0,END)
    lb1.insert(END,(client_name.get(),pg_name.get(),pitched_by.get(),amount.get(),college.get(),contact.get(),date_t.get(),commision.get()))

def get_row(event):
    try:
        global values
        index = lb1.curselection()[0]
        values = lb1.get(index)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        
        e1.insert(0,values[1])
        e2.insert(0,values[2])
        e3.insert(0,values[3])
        e4.insert(0,values[4])
        e5.insert(0,values[5])
        e6.insert(0,values[6])
        e7.insert(0,values[7])
        e8.insert(0,values[8])
    except IndexError:
        pass

lb1.bind("<<ListboxSelect>>",get_row)

def delete_comm():
    backend.delete(values[0])


#buttons
b1 = Button(window,text='View all',width=20,command=viewall,bg="medium aquamarine",bd=5)
b2 = Button(window,text='Search Entry',width=20,command=search_button,bg="medium aquamarine",bd=5)
b3 = Button(window,text='Add Entry',width=20,command=Add_entry,bg="medium aquamarine",bd=5)
b4 = Button(window,text='Update New',width=20,command=Add_entry,bg="medium aquamarine",bd=5)
b5 = Button(window,text='Delete',width=20,command=delete_comm,bg="medium aquamarine",bd=5)
b6 = Button(window,text='Close',width=20,command=window.destroy,bg="medium aquamarine",bd=5)
b1.grid(row=3,column=4)
b2.grid(row=4,column=4)
b3.grid(row=5,column=4)
b4.grid(row=6,column=4)
b5.grid(row=7,column=4)
b6.grid(row=8,column=4)



window.mainloop()