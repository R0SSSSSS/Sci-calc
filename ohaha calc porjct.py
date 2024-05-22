from tkinter import *
import math

root = Tk()
root.title("Scientific Calculator")
root.config(bg="grey")

e = Entry(root, width=40, borderwidth=10, fg="black", bg="yellowgreen")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


def button_click(b_click):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(b_click))
    
def Button_clear():
    e.delete(0, END)
    
def Button_addition():
    first_number = e.get()   
    global f_num
    global math_op
    math_op = "addition"
    f_num = float(first_number)
    e.delete(0, END)
    
def Button_subtraction():
    first_number = e.get()   
    global f_num
    global math_op
    math_op = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)    
  
def Button_multiply():
    first_number = e.get()   
    global f_num
    global math_op
    math_op = "multiply"
    f_num = float(first_number)
    e.delete(0, END)    
    
def Button_divide():
    first_number = e.get()   
    global f_num
    global math_op
    math_op = "division"
    f_num = float(first_number)
    e.delete(0, END)      

def Button_sqrt():
    first_number = e.get()
    e.delete(0, END)
    e.insert(0, math.sqrt(float(first_number)))
    
def Button_pow2():
    first_number = e.get()
    e.delete(0, END)
    e.insert(0, float(first_number)**2)
    
def Button_sin():
    first_number = e.get()
    e.delete(0, END)
    e.insert(0, math.sin(math.radians(float(first_number))))
    
def Button_cos():
    first_number = e.get()
    e.delete(0, END)
    e.insert(0, math.cos(math.radians(float(first_number))))
    
def Button_tan():
    first_number = e.get()
    e.delete(0, END)
    e.insert(0, math.tan(math.radians(float(first_number))))
    
def Button_equal():
    second_number = e.get()   
    e.delete(0, END) 
    
    if math_op == "addition":
        e.insert(0, f_num + float(second_number))
        
    if math_op == "subtraction":
        e.insert(0, f_num - float(second_number))
        
    if math_op == "multiply":
        e.insert(0, f_num * float(second_number))
        
    if math_op == "division":
        e.insert(0, f_num / float(second_number))
        
        
# Arithmetic operations
def switch_to_arithmetic():
    Button_Subtraction.config(command=Button_subtraction)
    Button_Division.config(command=Button_divide)
    Button_Multiply.config(command=Button_multiply)
    Button_Addition.config(command=Button_addition)
    Button_switch_operations.config(text="Switch to Trig Functions", command=switch_to_trig)

# Trigonometric functions
def switch_to_trig():
    Button_Subtraction.config(command=Button_sin)
    Button_Division.config(command=Button_cos)
    Button_Multiply.config(command=Button_tan)
    Button_Addition.config(command=Button_sqrt)
    Button_switch_operations.config(text="Switch to Arithmetic", command=switch_to_arithmetic)

# buttons
Button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1),borderwidth=5,bg="grey")
Button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2),borderwidth=5,bg="grey")
Button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3),borderwidth=5,bg="grey")
Button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4),borderwidth=5,bg="grey")
Button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5),borderwidth=5,bg="grey")
Button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6),borderwidth=5,bg="grey")
Button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7),borderwidth=5,bg="grey")
Button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8),borderwidth=5,bg="grey")
Button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9),borderwidth=5,bg="grey")
Button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0),borderwidth=5,bg="grey")
Button_Division = Button(root, text="/ | cos", padx=40, pady=20, command=Button_divide, fg="red",borderwidth=5,bg="grey")
Button_Multiply = Button(root, text="* | tan", padx=40, pady=20, command=Button_multiply, fg="red",borderwidth=5,bg="grey")
Button_Subtraction = Button(root, text="- | sin", padx=40, pady=20, command=Button_subtraction, fg="red",borderwidth=5,bg="grey")
Button_Addition = Button(root, text="+ | sqrt", padx=40, pady=20, command=Button_addition, fg="red",borderwidth=5,bg="grey")
Button_Equal = Button(root, text="=", padx=40, pady=20, command=Button_equal, fg="red",borderwidth=5,bg="grey")
Button_Clear = Button(root, text="Clear", padx=30, pady=20, command=Button_clear, fg="red",borderwidth=5,bg="grey")
Button_Pow2 = Button(root, text="x^2", padx=40, pady=20, command=Button_pow2, fg="red",borderwidth=5,bg="grey")
Button_switch_operations = Button(root, text="Switch to Trig Functions", padx=30, pady=20, command=switch_to_trig, fg="red", bg="grey",borderwidth=5)

# displaying the buttons
Button7.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
Button8.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
Button9.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
Button_Division.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

Button4.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
Button5.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
Button6.grid(row=2, column=2, padx=5, pady=5, sticky="ew")
Button_Multiply.grid(row=2, column=3, padx=5, pady=5, sticky="ew")

Button1.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
Button2.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
Button3.grid(row=3, column=2, padx=5, pady=5, sticky="ew")
Button_Subtraction.grid(row=3, column=3, padx=5, pady=5, sticky="ew")

Button0.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
Button_Clear.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
Button_Equal.grid(row=4, column=2, padx=5, pady=5, sticky="ew")
Button_Addition.grid(row=4, column=3, padx=5, pady=5, sticky="ew")

Button_Pow2.grid(row=5, column=3, padx=5, pady=5, sticky="ew")
Button_switch_operations.grid(row=5, column=0, columnspan=3, sticky="ew")

root.mainloop()
