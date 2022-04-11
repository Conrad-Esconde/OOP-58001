from tkinter import *
window=Tk()
window.title("Midterms in OOP")
Lbl1=Label( text="Enter your Full Name :", font=40)
Lbl1.place(x=100, y=150)
Lbl1=Label( text="", font=40)
Lbl1.place(x=6, y=8)

Ent=Entry(window)
Ent.place(x=350, y=150)

def C1():
    Ent.insert(0, "")
    Lbl2=Label(Lfm, text=Ent.get())
    Lbl2.pack()


Btn=Button(window, text="Click to Display Full Name :", font=40, command=C1)
Btn.place(x=100, y=200)

Lfm=Label(window)
Lfm.place(x=350, y=200)
window.title("OOp Midterm")
window.geometry("800x400+10+20")
window.mainloop()