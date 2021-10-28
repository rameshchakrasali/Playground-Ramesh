import tkinter
import calendar
from tkinter import *

#This function displays calendar for a given year
def showCalender():
    gui = Tk()
    gui.config(background='green')
    gui.title("Calender for the year")
    gui.geometry("300x200")
    year = int(year_field.get())
    gui_content= calendar.calendar(year)
    calYear = Label(gui, text= gui_content, font= "Times New Roman 10 bold")
    calYear.grid(row=5, column=1,padx=20)
    gui.mainloop()

#Driver code
if __name__=='__main__':
    new = Tk()
    new.config(background='Blue')
    new.title("Calender")
    new.geometry("500x500")
    cal = Label(new, text="Calender",bg='blue',font=("times", 28, "bold"))
    #Label for enter year
    year = Label(new, text="Enter year", bg='blue')
    #text box for year input
    year_field=Entry(new)
    button = Button(new, text='Show Calender',fg='yellow',bg='red',command=showCalender)

    #adjusting widgets in position
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    button.grid(row=6, column=1)
    new.mainloop()

