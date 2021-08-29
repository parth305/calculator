from tkinter import *


def click(event):
    global var
    text = event.widget.cget("text")
    if text == "+/-":
        if var.get()[0] != "-":
            value = "-" + var.get()
        else:
            value = var.get()[1:]
    elif text == "e":
        if var.get() != "Error":
            value = var.get()[:-1]
    elif text == "C":
        value = ""
    elif text == "=":
        try:
            value = str(eval(var.get()))
        except Exception as e:
            value = "Error"
    elif text == "":
        value = "0"
    else:
        value = var.get() + text
    var.set(value)


root = Tk()
root.geometry("355x480")
root.resizable(False, False)

var = StringVar()
var.set("")

label = Label(root, textvariable=var, width=420, font="lucida 40 bold", bg="red", anchor="w").pack()


def mybutton(f, number):
    button = Button(f, text=str(number), width=3, font="lucida 20 bold", padx=5, pady=5, anchor="w")
    button.pack(padx=10, pady=10, side=LEFT)
    button.bind("<Button>", click)
    return button


f1 = Frame(root, bg="black")
f2 = Frame(root, bg="black")
f3 = Frame(root, bg="black")
f4 = Frame(root, bg="black")
f5 = Frame(root, bg="black")

frames = [f1, f2, f3, f4, f5]
blist = ["C", "+/-", "e", "/", "9", "8", "7", "*", "6", "5", "4", "-", "3", "2", "1", "+", "00", "0", ".", "="]

j = 0
for frame in frames:
    for i in range(4):
        mybutton(frame, blist[j])
        j += 1
    frame.pack(anchor="w")

root.mainloop()
