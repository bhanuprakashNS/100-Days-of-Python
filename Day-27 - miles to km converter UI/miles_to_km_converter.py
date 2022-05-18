# ................... miles to km converter using Tkinter ................... #
# ........... Created and modified by NS Bhanuprakash on 05-04-2022 ......... #

from tkinter import *

screen = Tk()
screen.title(string="Miles to km converter")
screen.minsize(width=300, height=200)
screen.config(padx=50, pady=50)

Label_1 = Label(text="miles", font=("Arial", 15, "italic"))
Label_1.grid(row=0, column=2)
Label_2 = Label(text="km", font=("Arial", 15, "italic"))
Label_2.grid(row=1, column=2)
Label_3 = Label(text="is equal to", font=("Arial", 12, "italic"))
Label_3.grid(row=1, column=0)
# Label_4 = DoubleVar()
Label_4 = Label(text="", font=("Arial", 12, "bold"))
Label_4.grid(row=1, column=1)
Label_4.config(padx=20, pady=20)

miles = Entry(width=5)
miles.grid(row=0, column=1)


def miles_to_km():
    miles_value = float(miles.get())
    # print(miles_value)
    km_value = round(miles_value * 1.61, 1)
    # print(km_value)
    Label_4.config(text=f"{km_value}")


button_1 = Button(text="convert", command=miles_to_km)
button_1.grid(row=2, column=1)

screen.mainloop()
