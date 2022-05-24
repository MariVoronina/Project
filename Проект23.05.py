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
import investpy
import sqlite3
import json
import statistics


types = ["Banks", "Biotechnology", "Cars", "Hotels", "IT", "Entertainments", "Clothes", "Food"]
countries = ["United States", "Russia", "China", "United Kingdom", "France", "Japan"]
dict_types = {"Banks": "1", "Biotechnology": "2", "Cars": "3", "Hotels": "4", "IT": "5", "Entertainments": "6",
              "Clothes": "7", "Food": "8"}
dict_countries = {"United States": "1", "Russia": "2", "China": "3", "France": "4", "Japan": "5"}
dict_currency = {"United States": "USD", "Russia": "RUB", "China": "CNY", "France": "EUR", "Japan": "JPY"}
dict_transfer = {"USD": 1, "RUB": 64.74, "CNY": 0.16, "EUR": 1.04, "JPY": 0.0078}


stocks = sqlite3.connect("C:\\Users\\Моя госпожа\\Desktop\\Питонище\\Stocks.s3db")
cursor = stocks.cursor()


def info_stocks(country: str, type: str, date_from: str, date_to: str):
    tos = date_to.split("/")
    fro = date_from.split("/")
    if int(tos[2]) < 2012 or int(fro[2]) < 2012:
        return f"Date entered incorrectly"
    elif int(fro[2]) > int(tos[2]):
        return f"Date entered incorrectly"
    elif int(fro[2]) == int(tos[2]) and int(fro[1]) > int(tos[1]):
        return f"Date entered incorrectly"
    elif int(fro[2]) == int(tos[2]) and int(fro[1]) == int(tos[1]) and int(fro[0]) > int(tos[0]):
        return f"Date entered incorrectly"
    else:
        result = cursor.execute("select Code from Stocks where country=:code_count and type=:code_type",
                                {"code_count": dict_countries[country], "code_type": dict_types[type]})
        dict_result = {}
        for row in result:
            info = json.loads(investpy.get_stock_historical_data(stock=row[0], country=country, from_date=date_from,
                                to_date=date_to, as_json=True))
            if int(tos[2]) - int(fro[2]) == 0:
                if int(tos[1]) - int(fro[1]) == 0:
                    dict_result[info["name"]] = {}
                    for pr in info["historical"]:
                        dict_result[info["name"]][pr["date"].split("/")[0]] = pr["close"]
                elif int(tos[1]) - int(fro[1]) == 1:
                    dict_result[info["name"]] = {}
                    for pr in info["historical"]:
                        if fro[1] in pr["date"]:
                            dict_result[info["name"]][f"{pr['date'].split('/')[0]}/{fro[1]}"] = pr["close"]
                        elif tos[1] in pr["date"]:
                            dict_result[info["name"]][f"{pr['date'].split('/')[0]}/{tos[1]}"] = pr["close"]
                else:
                    list_result = []
                    for pr in info["historical"]:
                        list_result.append(pr["close"])
                    dict_result[info["name"]] = list_result
            elif int(fro[1]) == 12 and int(tos[1]) == 1 and int(tos[2]) - int(fro[2]) == 1:
                dict_result[info["name"]] = {}
                for pr in info["historical"]:
                    if fro[1] in pr["date"]:
                        dict_result[info["name"]][f"{pr['date'].split('/')[0]}/{fro[1]}/{fro[2][2:]}"] = pr["close"]
                    elif tos[1] in pr["date"]:
                        dict_result[info["name"]][f"{pr['date'].split('/')[0]}/{tos[1]}/{tos[2][2:]}"] = pr["close"]
            else:
                list_result = []
                for pr in info["historical"]:
                    list_result.append(pr["close"])
                dict_result[info["name"]] = list_result
        if dict_result == {}:
            return f"Unfortunately there are no companies of this type"
        return dict_result


def compare_stocks(country_1: str, country_2: str, type: str, date_from: str, date_to: str):
    info_1 = info_stocks(country_1, type, date_from, date_to)
    info_2 = info_stocks(country_2, type, date_from, date_to)
    if info_1 == f"Date entered incorrectly":
        return f"Date entered incorrectly"
    elif info_1 == f"Unfortunately there are no companies of this type" and \
            not info_2 == f"Unfortunately there are no companies of this type":
        return f"The stocks of {country_2} are more beneficial"
    elif not info_1 == f"Unfortunately there are no companies of this type" and \
            info_2 == f"Unfortunately there are no companies of this type":
        return f"The stocks of {country_1} are more beneficial"
    elif info_1 == f"Unfortunately there are no companies of this type" and \
            info_2 == f"Unfortunately there are no companies of this type":
        return f"Unfortunately there are no companies of this type"
    else:
        comp_1 = 0
        comp_2 = 0
        for i in info_1.keys():
            comp_1 += round(statistics.mean(info_1[i]) * dict_transfer[dict_currency[country_1]], 2)
        for i in info_2.keys():
            comp_2 += round(statistics.mean(info_2[i]) * dict_transfer[dict_currency[country_2]], 2)
        if comp_1 > comp_2:
            return f"The stocks of {country_1} are more beneficial than the stocks of {country_2}"
        elif comp_1 < comp_2:
            return f"The stocks of {country_2} are more beneficial than the stocks of {country_1}"
        else:
            return f"The stocks of both countries are beneficial"


def company_description(company: str):
    result = cursor.execute("select Description from Stocks where Name=:company", {"company": company})
    for row in result:
        return row[0]



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




def clicked2():
	print(var10.get())
	print(var11.get())
	print(var20.get())
	print(var30.get())
	print(var40.get())


def clicked1():
# df = pd.DataFrame(info_stocks(var1.get(), var2.get(), str(var3.get()), str(var4.get())),
    #                  columns=list(info_stocks(var1.get(), var2.get(), str(var3.get()), str(var4.get()))))
    #print(df)
    #df.plot(y=list(info_stocks(var1.get(), var2.get(),  str(var3.get()), str(var4.get())))).patch.set_facecolor('antiquewhite')
    #plt.gcf().canvas.set_window_title("График")  # меняем заголовок
    #plt.grid()  # выводим решётку (сетку)
    #plt.title('График акций')
    #plt.xlabel("Временной промежуток", fontsize=14, fontweight="bold")
    #plt.ylabel("Стоимость акции", fontsize=14, fontweight="bold")
    #plt.show()
    print(var1.get(), var2.get(), str(var3.get()), str(var4.get()))


print(info_stocks("Japan", "Food", "23/02/2020", "05/03/2020"))



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
button1 = Button(frame1, text="Построить график",font = ("Times New Roman", 25), command=clicked1).grid(column = 1, row =5)


# frame2
ttk.Label(frame2, text = 'Здесь Вы можете сравнить акции крупных компаний выбранного типа в двух выбранных странах за выбранный период времени.',
		wraplength=800, justify="center", background = 'coral', foreground ="white",
		font = ("Times New Roman", 20)).grid(row = 0, column = 0, columnspan=5, **{ 'ipadx': 10, 'ipady': 10 , 'sticky': 'nswe' })

ttk.Label(frame2, text = "Выберите первую страну:",
		font = ("Times New Roman", 25), background = 'darkorange', foreground ="lavenderblush").grid(column = 0,
		row = 1, padx = 10, pady = 25)
v10 = StringVar()
var10 = ttk.Combobox(frame2, width = 20, textvariable = v10, font=("Times New Roman", 20))
var10['values'] = countries
var10.grid(column = 1, row = 1)
var10.current()

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
v20 = StringVar()
var20 = ttk.Combobox(frame2, width = 20, textvariable = v20, font=("Times New Roman", 20))
var20['values'] = types
var20.grid(column = 1, row = 3)
var20.current()

ttk.Label(frame2, text = "Введите первый день:",
		font = ("Times New Roman", 25), background = 'darkorange', foreground ="lavenderblush").grid(column = 0,
		row = 4, padx = 10, pady = 25)
v30 = StringVar()
var30 = Entry(frame2, width = 20, textvariable = v30, font=("Times New Roman", 20))
var30.grid(column = 1, row = 4)

ttk.Label(frame2, text = "Введите последний день:",
		font = ("Times New Roman", 25), background = 'darkorange', foreground ="lavenderblush").grid(column = 0,
		row = 5, padx = 10, pady = 25)
v40 = StringVar()
var40 = Entry(frame2, width = 20, textvariable = v40, font=("Times New Roman", 20))
var40.grid(column = 1, row = 5)
button2 = Button(frame2, text="Построить график",font = ("Times New Roman", 25), command=clicked2).grid(column = 1, row =6)





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