import tkinter as tk
from tkinter import *
window =tk.Tk()
window.title("CALCULATOR")
window.geometry("570x600+100+200")
window.resizable(False,False)
window.configure(bg="#17161b")

equation= ""

#to show the values
def show(value):
    global equation
    equation+=value
    labal_result.config(text=equation)

#to clear the input or output 
def clear():
    global equation
    equation =""
    labal_result.config(text=equation)

#calculate the values
def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = str(eval(equation))
        except:
            result = "error"
            equation = ""
            labal_result.config(text="error")
    labal_result.config(text=result)


#input and also show result

labal_result = tk.Label(window, width=26, height=2, text="", font=("arial", 30))
labal_result.pack()

Button(window,text="c",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=10,y=100)
Button(window,text="/",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("/")).place(x=150,y=100)
Button(window,text="%",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("%")).place(x=290,y=100)
Button(window,text="*",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("*")).place(x=430,y=100)

Button(window,text="7",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("7")).place(x=10,y=200)
Button(window,text="8",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("8")).place(x=150,y=200)
Button(window,text="9",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("9")).place(x=290,y=200)
Button(window,text="-",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("-")).place(x=430,y=200)

Button(window,text="6",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("6")).place(x=10,y=300)
Button(window,text="5",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("5")).place(x=150,y=300)
Button(window,text="4",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("4")).place(x=290,y=300)
Button(window,text="+",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("+")).place(x=430,y=300)

Button(window,text="1",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("1")).place(x=10,y=400)
Button(window,text="2",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("2")).place(x=150,y=400)
Button(window,text="3",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("3")).place(x=290,y=400)
Button(window,text="0",width=11,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("0")).place(x=10,y=509)

Button(window,text=".",width=5,height=2,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show(".")).place(x=290,y=500)
Button(window, text="=", width=5, height=4, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: calculate()).place(x=430, y=400)


window.mainloop()
