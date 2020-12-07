import tkinter as tk #importing tkinter module
from tkinter import messagebox # importing messagebox where you can show any message

root = tk.Tk() #initializing the window
root.title("Calculator") #seeting the calculator

label = tk.Label(root, text="Enter first number",pady=(10)) #label for first value
label.pack() #packing the label

first_number_entry = tk.Entry(root) # box for input of first value
first_number_entry.pack()

label2 = tk.Label(root, text="Enter second number") # the second value
label2.pack()

second_number_entry = tk.Entry(root)
second_number_entry.pack()

operations = tk.Label(root, text="Operations")
operations.pack()

result_label = tk.Label(root, text="Operations result is:")
result_label.pack()

def addition():
    first, second = takeValueInput()
    result = first + second
    # print(first + second)
    result_label.config(text="Operations result is: " + #congiguration of result as per addition
                             str(result))

def subtract():
    first, second = takeValueInput()
    result = first - second
    # print(first + second)
    result_label.config(text="Operations result is: " +
                             str(result))

def multiply():
    first, second = takeValueInput()
    result = first * second
    # print(first + second)
    result_label.config(text="Operations result is: " +
                             str(result))

def divide():
    first, second = takeValueInput()
#EXCEPTION HANDLING
    if second == 0:
        messagebox.showerror("Error", "Cannot divide the value by 0.")
    else:
        result = first / second
        # print(first + second)
        result = round(result, 2)
        result_label.config(text="Operations result is: " +
                                 str(result))

def takeValueInput():
    first = first_number_entry.get()
    second = second_number_entry.get()

    try:
        first = int(first)
        second = int(second)

        return first, second
    except ValueError:
        if ((len(first_number_entry.get()) == 0) or (len(second_number_entry.get()) == 0)):
            messagebox.showerror("Error", "Please enter a value")
        else:
            messagebox.showerror("Error", "Enter only integer value")
        quit(0)

# the buttons for doing calculation
#such as Addition , substraction and all.
addition_button = tk.Button(root, text="+",
                            command=lambda : addition())
addition_button.pack()

minus_button = tk.Button(root, text="-",
                         command=lambda : subtract())
minus_button.pack()

multiply_button = tk.Button(root, text="*",
                            command=lambda : multiply())
multiply_button.pack()

division_button = tk.Button(root, text="/",
                            command=lambda : divide())
division_button.pack()



root.mainloop()