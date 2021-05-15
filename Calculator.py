from tkinter import *

if __name__ == "__main__":
    window = Tk()
    window.title("My Little Calculator")

    expression_field = Entry(window, width=30)
    expression_field.grid(row=0, column=0, columnspan=4)

    button7 = Button(window, text="7", height=3, width=3, borderwidth=1)
    button7.grid(row=1, column=0, sticky="ew")

    button8 = Button(window, text="8", height=3, width=3, borderwidth=1)
    button8.grid(row=1, column=1, sticky="ew")

    button9 = Button(window, text="9", height=3, width=3, borderwidth=1)
    button9.grid(row=1, column=2, sticky="ew")

    divisionButton = Button(window, text="/", height=3, width=3, borderwidth=1)
    divisionButton.grid(row=1, column=3, sticky="ew")

    button1 = Button(window, text="1", height=3, width=3, borderwidth=1)
    button1.grid(row=1, column=0, sticky="ew")

    button2 = Button(window, text="2", height=3, width=3, borderwidth=1)
    button2.grid(row=1, column=1, sticky="ew")

    button3 = Button(window, text="3", height=3, width=3, borderwidth=1)
    button3.grid(row=1, column=2, sticky="ew")

    multiplicationButton = Button(window, text="*", height=3, width=3, borderwidth=1)
    multiplicationButton.grid(row=1, column=3, sticky="ew")

    button1 = Button(window, text="1", height=3, width=3, borderwidth=1)
    button1.grid(row=1, column=0, sticky="ew")

    button2 = Button(window, text="2", height=3, width=3, borderwidth=1)
    button2.grid(row=1, column=1, sticky="ew")

    button3 = Button(window, text="3", height=3, width=3, borderwidth=1)
    button3.grid(row=1, column=2, sticky="ew")

    multiplicationButton = Button(window, text="*", height=3, width=3, borderwidth=1)
    multiplicationButton.grid(row=1, column=3, sticky="ew")

    window.mainloop()