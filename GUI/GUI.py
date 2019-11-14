from tkinter import *

window=Tk()

l1=Label(window ,text="Title")
l1.grid( row=0 , column=0)


l1=Label(window ,text="Year")
l1.grid( row=2 , column=0)

l1=Label(window ,text="Label")
l1.grid( row=0 , column=4)


l1=Label(window ,text="ISBL")
l1.grid( row=2 , column=4)

title_text=StringVar()
e1=Entry(window ,textvariable=title_text)
e1.grid(row=0 ,column=1)


year_text=StringVar()
e2=Entry(window ,textvariable=year_text)
e2.grid(row=0 ,column=3)

label_text=StringVar()
e2=Entry(window ,textvariable=label_text)
e2.grid(row=1,column=1)




ISB_text=StringVar()
e2=Entry(window ,textvariable=ISB_text)
e2.grid(row=1 ,column=3)


window.mainloop()

