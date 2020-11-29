import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
root.title("Calculator By @AaryanSarda")

expression = ""

def add(value) :
    global expression
    expression += value
    label_result.config(text=expression)
    

def clear():
    global expression
    expression = ""
    label_result.config(text=expression)

def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
            label_result.config(text=result)
        except:
            result = "error"
            expression = ""
            tk.messagebox.showerror(title="Error", message="expression you entered does not have perfect terms")
    label_result.config(text=result)

#Create GUI

label_result = tk.Label(root, text="")
label_result.grid(row=0, column=0, columnspan=4)

button_1 = tk.Button(root, text="1", command=lambda: add("1"), width=5)
button_1.grid(row=1, column=0)

button_2 = tk.Button(root, text="2", command=lambda: add("2"), width=5)
button_2.grid(row=1, column=1)

button_3 = tk.Button(root, text="3", command=lambda: add("3"), width=5)
button_3.grid(row=1, column=2)

button_divide = tk.Button(root, text="/", command=lambda: add("/"), width=5)
button_divide.grid(row=1, column=3)


button_4 = tk.Button(root, text="4", command=lambda: add("4"), width=5)
button_4.grid(row=2, column=0)

button_5 = tk.Button(root, text="5", command=lambda: add("5"), width=5)
button_5.grid(row=2, column=1)

button_6 = tk.Button(root, text="6", command=lambda: add("6"), width=5)
button_6.grid(row=2, column=2)

button_multiply = tk.Button(root, text="*", command=lambda: add("*"), width=5)
button_multiply.grid(row=2, column=3)


button_7 = tk.Button(root, text="7", command=lambda: add("7"), width=5)
button_7.grid(row=3, column=0)

button_8 = tk.Button(root, text="8", command=lambda: add("8"), width=5)
button_8.grid(row=3, column=1)

button_9 = tk.Button(root, text="9", command=lambda: add("9"), width=5)
button_9.grid(row=3, column=2)

button_subtract = tk.Button(root, text="-", command=lambda: add("-"), width=5)
button_subtract.grid(row=3, column=3)


button_clear = tk.Button(root, text="C", command=lambda: clear(), width=5)
button_clear.grid(row=4, column=0)

button_0 = tk.Button(root, text="0", command=lambda: add("0"), width=5)
button_0.grid(row=4, column=1)

button_decimal = tk.Button(root, text=".", command=lambda: add("."), width=5)
button_decimal.grid(row=4, column=2)

button_add = tk.Button(root, text="+", command=lambda: add("+"), width=5)
button_add.grid(row=4, column=3)

button_sq_root = tk.Button(root, text="√", command=lambda: add("**0.5"), width=5)
button_sq_root.grid(row=5, column=0)

button_sq = tk.Button(root, text="x²", command=lambda: add("**2"), width=5)
button_sq.grid(row=5, column=1)

button_cube = tk.Button(root, text="x³", command=lambda: add("**3"), width=5)
button_cube.grid(row=5, column=2)

button_cube = tk.Button(root, text="³√", command=lambda: add("**(1/3)"), width=5)
button_cube.grid(row=5, column=3)

button_equals = tk.Button(root, text="=", width=25, command=lambda: calculate())
button_equals.grid(row=7, column=0, columnspan=4)


root.mainloop()