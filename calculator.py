#import tkinter component 
import tkinter

#define the buttons function
def buttonClick(number):
    text.insert('end',str(number))

#empty entry 
def empty(letter):
    text.delete(0, 'end')

#define equal sign function
def equal():
    num = float(eval(text.get()))
    text.delete(0, 'end')
    text.insert('end',num)

top = tkinter.Tk()

# Post Label, Entry, Buttons on the window    
result = tkinter.Label(top, text="Result",font = ("Arial", 10, "bold"),  height=3, width=5)
result.grid(row = 0, column = 0)

text = tkinter.Entry(top, bd = 3)
text.grid(row=0, column = 1, columnspan=3)

num0 = tkinter.Button(top,text="0", height=3, width=5, command = lambda: buttonClick(0))
num0.grid(row = 1, column = 0)
num1 = tkinter.Button(top,text="1",height=3, width=5,command = lambda:buttonClick(1))
num1.grid(row = 1, column = 1)
num2 = tkinter.Button(top,text="2", height=3, width=5,command = lambda:buttonClick(2))
num2.grid(row = 1, column = 2)
num3 = tkinter.Button(top,text="3", height=3, width=5,command = lambda:buttonClick(3))
num3.grid(row = 1, column = 3)
num4 = tkinter.Button(top,text="4", height=3, width=5,command = lambda:buttonClick(4))
num4.grid(row = 2, column = 0)
num5 = tkinter.Button(top,text="5", height=3, width=5,command = lambda:buttonClick(5))
num5.grid(row = 2, column = 1)
num6 = tkinter.Button(top,text="6", height=3, width=5,command = lambda:buttonClick(6))
num6.grid(row = 2, column = 2)
num7 = tkinter.Button(top,text="7", height=3, width=5,command = lambda:buttonClick(7))
num7.grid(row = 2, column = 3)
num8 = tkinter.Button(top,text="8", height=3, width=5,command = lambda:buttonClick(8))
num8.grid(row = 3, column = 0)
num9 = tkinter.Button(top,text="9", height=3, width=5,command = lambda:buttonClick(9))
num9.grid(row = 3, column = 1)

# + button
add = tkinter.Button(top,text="+", height=3, width=5, command = lambda: buttonClick("+"))
add.grid(row = 3, column = 2)

# - button
substract = tkinter.Button(top,text="-", height=3, width=5,command = lambda: buttonClick("-"))
substract.grid(row = 3, column = 3)

# * button
multiply = tkinter.Button(top,text="*", height=3, width=5, command = lambda: buttonClick("*"))
multiply.grid(row = 4, column = 0)

# / button
divide = tkinter.Button(top,text="/", height=3, width=5, command = lambda: buttonClick("/"))
divide.grid(row = 4, column = 1)

# = button
equalButton = tkinter.Button(top,text="=", height=3, width=5, command = lambda: equal())
equalButton.grid(row = 4, column = 2)

# c button
setZero = tkinter.Button(top,text="c", height=3, width=5, command =lambda: empty("c"))
setZero.grid(row = 4, column = 3)
setZero.config (bg='light green')

top.title("Calculator")
top.mainloop()

