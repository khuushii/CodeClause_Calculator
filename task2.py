#CALCULATOR
from tkinter import *
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(END, str(result))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")

page = Tk()
page.title("Calculator")

bg_color = "#9BA4B5"  
button_bg_color = "#394867"  
button_fg_color = "#ffffff"  
entry_bg_color = "#212A3E"  
entry_fg_color = "#F1F6F9"  

page.configure(bg=bg_color)

#entry field
entry = Entry(page, width=25, borderwidth=5, bg=entry_bg_color, fg=entry_fg_color)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

#button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(number))


row = 1
col = 0
for button in buttons:
    if button == "=":
        btn = Button(page, text=button, padx=20, pady=10, bg=button_bg_color, fg=button_fg_color, command=calculate)
    else:
        btn = Button(page, text=button, padx=20, pady=10, bg=button_bg_color, fg=button_fg_color,
                     command=lambda num=button: button_click(num))
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1
page.mainloop()
