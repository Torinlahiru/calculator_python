import tkinter as tk

root = tk.Tk()

root.geometry("300x275")

cal =" "

def add(symble):
    global cal
    cal += str(symble)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,cal)

text_result = tk.Text(root,width=16,height=2,font=("Arial",24))
text_result.grid(columnspan=5)

btn1 = tk.Button(root,text="1",command=lambda:add(1),width=5,font=("Arial",14))
btn1.grid(row=2,column=1)
btn2 = tk.Button(root,text="2",command=lambda:add(2),width=5,font=("Arial",14))
btn2.grid(row=2,column=2)
btn3 = tk.Button(root,text="3",command=lambda:add(3),width=5,font=("Arial",14))
btn3.grid(row=2,column=3)
btn4 = tk.Button(root,text="4",command=lambda:add(4),width=5,font=("Arial",14))
btn4.grid(row=3,column=1)
btn5 = tk.Button(root,text="5",command=lambda:add(5),width=5,font=("Arial",14))
btn5.grid(row=3,column=2)
btn6 = tk.Button(root,text="6",command=lambda:add(6),width=5,font=("Arial",14))
btn6.grid(row=3,column=3)
btn7 = tk.Button(root,text="7",command=lambda:add(7),width=5,font=("Arial",14))
btn7.grid(row=4,column=1)
btn8 = tk.Button(root,text="8",command=lambda:add(8),width=5,font=("Arial",14))
btn8.grid(row=4,column=2)
btn9 = tk.Button(root,text="9",command=lambda:add(9),width=5,font=("Arial",14))
btn9.grid(row=4,column=3)
btn0 = tk.Button(root,text="0",command=lambda:add(0),width=5,font=("Arial",14))
btn0.grid(row=5,column=2)
root.mainloop()
