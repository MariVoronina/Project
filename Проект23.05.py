from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter import Menu
from tkinter import ttk
from tkinter.ttk import Notebook, Style
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def clicked3():
    fig, ax = plt.subplots()
    x = np.linspace(-5, 5, 25)
    y1 = x ** 2
    y2 = np.sin(x)
    y3 = 5 * x
    y4 = - x / 5
    ax.plot(x, y1)
    ax.plot(x, y2)
    ax.plot(x, y3)
    ax.plot(x, y4)
    plt.xlabel("Временной промежуток", fontsize=14, fontweight="bold")
    plt.ylabel("Стоимость акции", fontsize=14, fontweight="bold")
    plt.show()

types = ["Banks", "Biotechnology", "Cars", "Hotels", "IT", "Entertainments", "Clothes", "Food"]
countries = ["United States", "Russia", "China", "United Kingdom", "France", "Japan"]








window = Tk()
window.title("Акации по акции")
window.geometry('600x450')
#style = Style()
#style.theme_use('default')
#style.configure('TNotebook.Tab', background="greenyellow", font=('URW Gothic L','25','bold'))
#tab_control = ttk.Notebook(window) #, width=500, height=500
#tab1 = ttk.Frame(tab_control)
#tab2 = ttk.Frame(tab_control)
#tab_control.add(tab1, text='Первая')
#tab_control.add(tab2, text='Вторая')
#lbl1 = Label(tab1, text='Так норм?', font=("Arial Bold", 50))
#lbl1.grid(column=0, row=0)
#lbl2 = Label(tab2, text='Или может так?', font=("Arial Bold", 70))
#lbl2.grid(column=0, row=0)
#tab_control.pack(expand=1, fill='both')
menu = Menu(window)
new_item = Menu(menu)
strana = Menu(new_item)
new_item.add_command(label='График', command=clicked3)
new_item.add_separator()
for i in countries:
    strana.add_command(label=i)
    strana.add_separator()
new_item.add_cascade(label='по странам', menu=strana)
new_item.add_separator()
kategoria = Menu(new_item)
for i in types:
    kategoria.add_command(label=i)
    kategoria.add_separator()
new_item.add_cascade(label='по категориям', menu=kategoria)
menu.add_cascade(label='Сортировать', menu=new_item)
window.config(menu=menu)
#from PIL import ImageTk, Image
#img = Image.open('конор.jpg')
#width = 600
#ratio = (width / float(img.size[0]))
#height = int((float(img.size[1]) * float(ratio)))
#imag = img.resize((width, height), Image.ANTIALIAS)
#image = ImageTk.PhotoImage(imag)
#panel = Label(window, image=image)
#panel.pack(side="top", fill="both", expand="no")
window.mainloop()

import tkinter as tk
from tkinter import ttk


def clicked():
	print(var1.get())
	print(var2.get())
	print(var3.get())
	print(var4.get())


types = ["Banks", "Biotechnology", "Cars", "Hotels", "IT", "Entertainments", "Clothes", "Food"]
countries = ["United States", "Russia", "China", "United Kingdom", "France", "Japan"]

# Creating tkinter window
window = tk.Tk()
window.title('Акции')
window.geometry('800x750')
style = Style()
style.theme_use('default')
style.configure('TNotebook.Tab', background="greenyellow", font=('URW Gothic L','25','bold'))


# Create a Notebook widget
note =Notebook(window)

# Add a frame for adding a new tab
frame1= Frame(note, width= 800, height=750)
frame1.configure(background='moccasin')
# Adding the Tab Name
note.add(frame1, text= 'Получить данные')
frame2 = Frame(note, width= 800, height=750)
frame2.configure(background='moccasin')
note.add(frame2, text= "Сравнить данные")


# frame1
ttk.Label(frame1, text = "Здесь Вы можете получить данные по акциям крупных компаний выбранного типа в выбранной стране в течении выбранного периода, которые будут представлены в виде графика.",
		wraplength=800, justify="center", background = 'coral', foreground ="white",
		font = ("Times New Roman", 20)).grid(row = 0, column = 0, columnspan=5, **{ 'ipadx': 10, 'ipady': 10 , 'sticky': 'nswe' })

ttk.Label(frame1, text = "Выберите страну:",
		font = ("Times New Roman", 25), background = 'darkorange', foreground ="lavenderblush").grid(column = 0,
		row = 1, padx = 10, pady = 25)
v1 = StringVar()
var1 = ttk.Combobox(frame1, width = 20, textvariable = v1, font=("Times New Roman", 20))
var1['values'] = countries
var1.grid(column = 1, row = 1)
var1.current()

ttk.Label(frame1, text = "Выберите тип:",
		font = ("Times New Roman", 25), background = 'darkorange', foreground ="lavenderblush").grid(column = 0,
		row = 2, padx = 10, pady = 25)
v2 = StringVar()
var2 = ttk.Combobox(frame1, width = 20, textvariable = v2, font=("Times New Roman", 20))
var2['values'] = types
var2.grid(column = 1, row = 2)
var2.current()

ttk.Label(frame1, text = "Введите первый день:",
		font = ("Times New Roman", 25), background = 'darkorange', foreground ="lavenderblush").grid(column = 0,
		row = 3, padx = 10, pady = 25)
v3 = StringVar()
var3 = Entry(frame1, width = 20, textvariable = v3, font=("Times New Roman", 20))
var3.grid(column = 1, row = 3)

ttk.Label(frame1, text = "Введите последний день:",
		font = ("Times New Roman", 25), background = 'darkorange', foreground ="lavenderblush").grid(column = 0,
		row = 4, padx = 10, pady = 25)
v4 = StringVar()
var4 = Entry(frame1, width = 20, textvariable = v4, font=("Times New Roman", 20))
var4.grid(column = 1, row = 4)
button = Button(frame1, text="Построить график",font = ("Times New Roman", 25), command=clicked).grid(column = 1, row =5)


# frame2
ttk.Label(frame2, text = 'Здесь Вы можете сравнить акции крупных компаний выбранного типа в двух выбранных странах за выбранный период времени.',
		wraplength=800, justify="center", background = 'coral', foreground ="white",
		font = ("Times New Roman", 20)).grid(row = 0, column = 0, columnspan=5, **{ 'ipadx': 10, 'ipady': 10 , 'sticky': 'nswe' })

ttk.Label(frame2, text = "Выберите первую страну:",
		font = ("Times New Roman", 25), background = 'darkorange', foreground ="lavenderblush").grid(column = 0,
		row = 1, padx = 10, pady = 25)
v1 = StringVar()
var1 = ttk.Combobox(frame2, width = 20, textvariable = v1, font=("Times New Roman", 20))
var1['values'] = countries
var1.grid(column = 1, row = 1)
var1.current()

ttk.Label(frame2, text = "Выберите вторую страну:",
		font = ("Times New Roman", 25), background = 'darkorange', foreground ="lavenderblush").grid(column = 0,
		row = 2, padx = 10, pady = 25)
v11 = StringVar()
var11 = ttk.Combobox(frame2, width = 20, textvariable = v11, font=("Times New Roman", 20))
var11['values'] = countries
var11.grid(column = 1, row = 2)
var11.current()

ttk.Label(frame2, text = "Выберите тип:",
		font = ("Times New Roman", 25), background = 'darkorange', foreground ="lavenderblush").grid(column = 0,
		row = 3, padx = 10, pady = 25)
v2 = StringVar()
var2 = ttk.Combobox(frame2, width = 20, textvariable = v2, font=("Times New Roman", 20))
var2['values'] = types
var2.grid(column = 1, row = 3)
var2.current()

ttk.Label(frame2, text = "Введите первый день:",
		font = ("Times New Roman", 25), background = 'darkorange', foreground ="lavenderblush").grid(column = 0,
		row = 4, padx = 10, pady = 25)
v3 = StringVar()
var3 = Entry(frame2, width = 20, textvariable = v3, font=("Times New Roman", 20))
var3.grid(column = 1, row = 4)

ttk.Label(frame2, text = "Введите последний день:",
		font = ("Times New Roman", 25), background = 'darkorange', foreground ="lavenderblush").grid(column = 0,
		row = 5, padx = 10, pady = 25)
v4 = StringVar()
var4 = Entry(frame2, width = 20, textvariable = v4, font=("Times New Roman", 20))
var4.grid(column = 1, row = 5)
button = Button(frame2, text="Построить график",font = ("Times New Roman", 25), command=clicked).grid(column = 1, row =6)





note.pack(expand= True, fill=BOTH)
window.mainloop()



window = Tk()
window.title("Акации по акции")
window.geometry('800x200')
style = Style()
style.theme_use('default')
style.configure('TNotebook.Tab', background="greenyellow", font=('URW Gothic L','25','bold'))
tab_control = ttk.Notebook(window) #, width=500, height=500
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Получить данные')
tab_control.add(tab2, text='Сравнить данные')

lbl1 = Label(tab1, text='Здесь Вы можете получить данные по акциям крупных компаний выбранного типа '
						'в выбранной стране в течении выбранного периода, которые будут представлены в виде графика.', font=("Arial Bold", 15), wraplength=800, justify="center")
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text='Здесь Вы можете сравнить акции крупных компаний выбранного типа в двух выбранных '
						'странах за выбранный период времени.', font=("Arial Bold", 15), wraplength=800, justify="center")
lbl2.grid(column=0, row=0)


tab3 = ttk.Frame(tab_control)
lbl3 = Label(tab1, text='Страна:', font=("Arial Bold", 15))
lbl3.grid(column=0, row=5)
# Combobox creation
n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)

# Adding combobox drop down list
monthchoosen['values'] = (' January',
						' February',
						' March',
						' April',
						' May',
						' June',
						' July',
						' August',
						' September',
						' October',
						' November',
						' December')

monthchoosen.grid(column = 1, row = 5, padx = 10, pady = 25) #, padx = 10, pady = 25
monthchoosen.pack(side="bottom")

tab_control.pack(fill='both', side="top")
window.mainloop()