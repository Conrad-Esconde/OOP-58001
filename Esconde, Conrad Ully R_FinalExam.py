from tkinter import *                                # Tkinter module
window = Tk()                                        # Window
window.title("Find the least number")                # Title
window.geometry("280x200+20+100")                    # window dimensions

def findLeastNumber():                               # Functions
    L = []
    L.append(eval(number1.get()))                    # append to add item to list
    L.append(eval(number2.get()))                    # eval is to evaluate any arbitrary expressions
    L.append(eval(number3.get()))
    LeastNum.set(min(L))                             # Is used to return the smallest Item in iterable

lb1 = Label(window, text = "Input 3 numbers")         # label to prompt the user of direction
lb1.grid(row=0, column=0, columnspan=2,sticky=EW)     # position of Label1

lb2 = Label(window,text = "Enter the first number:")  # label 2
lb2.grid(row=1, column = 0,sticky=W)                  # position of Label2
number1 = StringVar()                                 # Can hold string Value, default is empty string , Cannot use IntVar , cause IntVar default is (0)
ent = Entry(window,bd=3,textvariable=number1)         # entry widget
ent.grid(row=1, column = 1)                           # position of Entry Widget

lb3 = Label(window,text = "Enter the second number:") # label 3
lb3.grid(row=2, column=0)                             # position of Label3
number2=StringVar()                                   # Can hold string Value, default is empty string , Cannot use IntVar , cause IntVar default is (0)
en2 = Entry(window,bd=3,textvariable=number2)         # entry widget 2
en2.grid(row=2,column=1)                              # position of Entry Widget 2

lb4 = Label(window,text="Enter the third number:")    # label 4
lb4.grid(row=3,column =0, sticky=W)                   # position of Label 4
number3 = StringVar()                                 # Can hold string Value, default is empty string , Cannot use IntVar , cause IntVar default is (0)
en3 = Entry(window,bd=3,textvariable=number3)         # entry widget 3
en3.grid(row=3, column=1)                             # position of Entry Widget 3

btn = Button(window,text = "Find the least no.",command=findLeastNumber)    # Button widget with the command that will Fint the Least No.
btn.grid(row=4, column = 1)                                                 # Position of the Button Widget

lb5 = Label(window,text="The Least number is:")                     # Label 5
lb5.grid(row=5,column=0,sticky=W)                                   # Position of Label 5
LeastNum = StringVar()                                              # To Manage the value of the Widget in Entry 4 (en4)
en4 = Entry(window,bd=3,state="readonly",textvariable=LeastNum)     # Entry 4 as a 'readonly' widget
en4.grid(row=5,column=1)                                            # position of Entry 4

mainloop()