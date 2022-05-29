import tkinter as tk # библиотека для работы с оконным приложением
from tkinter import *
from tkinter import messagebox # подмодуль для работы с диалоговым окном
from tkinter import ttk # модуль, содержащий классы виджетов и методы для изменения их внешнего вида
from PIL import ImageTk, Image # библиотека и модули для обработки изображений
from tkinter.ttk import Combobox # подмодуль для работы с выпадающим списком
from tkinter.ttk import Radiobutton # подмодуль для выбора одного из вариантов списка
from tkinter.ttk import Notebook # подмодуль для работы со вкладками в оконном приложении
from tkinter.ttk import Style # класс для работы со стилем
import matplotlib.pyplot as plt # библиотека для визуализации данных в виде графика
import pandas as pd # модуль для обработки и анализа данных
import investpy # пакет, откуда получаем информацию по рыночным ценам акций
import sqlite3 # модуль для работы с базой данных
import json # модуль для работы типом json
import statistics # модуль, в котором реализован метод mean()



types = ["Banks", "Biotechnology", "Cars", "Hotels", "IT", "Entertainments", "Clothes", "Food"] # типы компаний
countries = ["United States", "Russia", "China", "France", "Japan"] # названия стран
dict_types = {"Banks": "1", "Biotechnology": "2", "Cars": "3", "Hotels": "4", "IT": "5", "Entertainments": "6",
              "Clothes": "7", "Food": "8"} # коды названий компаний, которые им присвоены в базе данных
dict_countries = {"United States": "1", "Russia": "2", "China": "3", "France": "4", "Japan": "5"} # коды стран, которые им присвоены в базе данных
dict_currency = {"United States": "USD", "Russia": "RUB", "China": "CNY", "France": "EUR", "Japan": "JPY"} # валюта каждой из наших стран
dict_transfer = {"USD": 1, "RUB": 64.74, "CNY": 0.16, "EUR": 1.04, "JPY": 0.0078} # сколько долларов в единице данной валюты



stocks = sqlite3.connect("C:\\stocks\\Stocks.s3db") # соединение с базой данных
cursor = stocks.cursor() # объект для работы с базой данных: формирования запросов поиска, добавления, удаления и т.д.

# функция, которая возвращает информацию по рыночным ценам акций компаний выбранного типа в выбраной стране в течении выбранного периода времени
def info_stocks(country: str, type: str, date_from: str, date_to: str):
    tos = date_to.split("/")
    fro = date_from.split("/")
    # проверка на правильность ввода даты
    if int(tos[1]) >= 13 or int(fro[1]) >= 13 or int(tos[0]) >= 32 or int(fro[0]) >= 32:
        messagebox.showerror("Error", "Date entered incorrectly") # вывод диалогового окна с информацией
        return f"Date entered incorrectly"
    elif int(tos[2]) < 2012 or int(fro[2]) < 2012:
        messagebox.showerror("Error", "Date entered incorrectly")
        return f"Date entered incorrectly"
    elif int(fro[2]) > int(tos[2]):
        messagebox.showerror("Error", "Date entered incorrectly")
        return f"Date entered incorrectly"
    elif int(fro[2]) == int(tos[2]) and int(fro[1]) > int(tos[1]):
        messagebox.showerror("Error", "Date entered incorrectly")
        return f"Date entered incorrectly"
    elif int(fro[2]) == int(tos[2]) and int(fro[1]) == int(tos[1]) and int(fro[0]) > int(tos[0]):
        messagebox.showerror("Error", "Date entered incorrectly")
        return f"Date entered incorrectly"
    else:
        # формирование запроса по выбору из базы данных из поля Code компаний, у которых страна и тип совпадают с выбранными
        result = cursor.execute("select Code from Stocks where country=:code_count and type=:code_type",
                                {"code_count": dict_countries[country], "code_type": dict_types[type]})
        dict_result = {} # наш будущий результат
        for row in result:
            info = json.loads(investpy.get_stock_historical_data(stock=row[0], country=country, from_date=date_from,
                                to_date=date_to, as_json=True)) # получаем информацию в формате json и преобразуем в словарь
            # формируем словарь для красивого вывода графика
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
            # формируем словарь для большого периода
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
        # проверка на отсутствие информации
        if dict_result == {}:
            return f"Unfortunately there are no companies of this type"
        return dict_result # возвращаем результат

# функция для сравнения рыночных цен акций выбранного типа компаний в двух выбранных странах в течении выбранного периода времени
def compare_stocks(country_1: str, country_2: str, typen: str, date_from: str, date_to: str):
    info_1 = info_stocks(country_1, typen, date_from, date_to)
    info_2 = info_stocks(country_2, typen, date_from, date_to)
    # проверка на неправильно введённую дату
    if info_1 == f"Date entered incorrectly":
        return f"Date entered incorrectly"
    # проверка на отсутствие информации
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
        comp_1 = 0  # будущий результат в первой стране
        comp_2 = 0  # будущий результат во второй стране
        # высчитываем среднее арифметическое по всем рыночным ценам акций в первой стране
        for i in info_1.keys():
            if type(info_1[i]) is dict:
                comp_1 += round(statistics.mean(info_1[i].values()) * dict_transfer[dict_currency[country_1]], 2)
            else:
                comp_1 += round(statistics.mean(info_1[i]) * dict_transfer[dict_currency[country_1]], 2)
        # высчитываем среднее арифметическое по всем рыночным ценам акций во второй стране
        for i in info_2.keys():
            if type(info_2[i]) is dict:
                comp_2 += round(statistics.mean(info_2[i].values()) * dict_transfer[dict_currency[country_2]], 2)
            else:
                comp_2 += round(statistics.mean(info_2[i]) * dict_transfer[dict_currency[country_2]], 2)
        # сравнение и выдача окончательного результата
        if comp_1 > comp_2:
            return f"The stocks of {country_1} are more beneficial than the stocks of {country_2}"
        elif comp_1 < comp_2:
            return f"The stocks of {country_2} are more beneficial than the stocks of {country_1}"
        else:
            return f"The stocks of both countries are beneficial"


# функция, возвращающая профиль компании
def company_description(company: str):
    # формирование запроса по поиску в базе данных такой компании
    result = cursor.execute("select Description from Stocks where Name=:company", {"company": company})
    # передвигаемся по выбранным строкам и возвращаем описание
    for row in result:
        return row[0]


# функция, выводящая график акций компаний, исходя из введенных пользователем данных
def clicked1():
    df = pd.DataFrame(info_stocks(var1.get(), var2.get(), str(var3.get()), str(var4.get())),
                      columns=list(info_stocks(var1.get(), var2.get(), str(var3.get()), str(var4.get())))) # создаем табличную структуру данных
    df.plot(y=list(info_stocks(var1.get(), var2.get(),  str(var3.get()), str(var4.get())))).patch.set_facecolor('antiquewhite') # по табличной структуре строим график
    plt.grid()  # выводим сетку
    plt.title('Stock chart of '+ var1.get()) # задаем название графика
    plt.xlabel("Time interval", fontsize=14, fontweight="bold") # выводим подпись оси X
    plt.ylabel("Stock value, "+ dict_currency[var1.get()], fontsize=14, fontweight="bold") # выводим подпись оси Y
    plt.show() # выводим график

# функция, выводящая графики акций каждой из двух заданных стран для сравнения
def clicked2():
    df1 = pd.DataFrame(info_stocks(var10.get(), var20.get(), str(var30.get()), str(var40.get())),
                      columns=list(info_stocks(var10.get(), var20.get(), str(var30.get()), str(var40.get()))))
    df1.plot(y=list(info_stocks(var10.get(), var20.get(), str(var30.get()), str(var40.get())))).patch.set_facecolor(
        'antiquewhite')
    plt.grid()
    plt.title('Stock chart of '+ var10.get())
    plt.xlabel("Time interval", fontsize=14, fontweight="bold")
    plt.ylabel("Stock value, " + dict_currency[var10.get()], fontsize=14, fontweight="bold")

    df2 = pd.DataFrame(info_stocks(var11.get(), var20.get(), str(var30.get()), str(var40.get())),
                      columns=list(info_stocks(var11.get(), var20.get(), str(var30.get()), str(var40.get()))))
    df2.plot(y=list(info_stocks(var11.get(), var20.get(), str(var30.get()), str(var40.get())))).patch.set_facecolor(
        'antiquewhite')
    plt.grid()
    plt.title('Stock chart of ' + var11.get())
    plt.xlabel("Time interval", fontsize=14, fontweight="bold")
    plt.ylabel("Stock value, " + dict_currency[var11.get()], fontsize=14, fontweight="bold")
    plt.show()
    messagebox.showinfo('Summary', compare_stocks(var10.get(), var11.get(), var20.get(), str(var30.get()), str(var40.get())))
    # выводим сообщение о том, акции какой страны в среднем выгоднее

# функция, выводящая окно с информацией о компаниях
def clicked3():
    wind = tk.Tk() # создаем окно
    wind.title('Information about companies') # задаем название окна
    wind.geometry('800x750') # задаем размер окна
    wind.configure(bg='linen') # задаем цвет фона
    # исходя из выбранной страны, типа компании и периода, получаем информацию о компаниях и последовательно добавляем их в окно
    for i in range(len(list(info_stocks(var1.get(), var2.get(), str(var3.get()), str(var4.get()))))):
        ttk.Label(wind,
                  text=str(company_description(list(info_stocks(var1.get(), var2.get(), str(var3.get()), str(var4.get())))[i]))+"\n"+"\n",
                  wraplength=800, justify="center", background='linen', foreground="maroon",
                  font=("Times New Roman", 20)).grid(row=i, column=0)

    wind.mainloop()



window = tk.Tk()
window.title('Stocks')
window.geometry('900x650')
style = Style()
style.theme_use('default')
style.configure('TNotebook.Tab', background="linen", font=('URW Gothic L','25','bold')) # неактивная вкладка окна будет цвета linen


note = Notebook(window) # создаем виджет Notebook
frame1 = Frame(note, width= 1000, height=700) # добавляем рамку для первой вкладки
frame1.configure(background="linen")
note.add(frame1, text= 'Price analysis') # добавляем имя вкладки
frame2 = Frame(note, width= 1000, height=700) # добавляем рамку для второй вкладки
frame2.configure(background='linen')
note.add(frame2, text= "Price comparison")


# frame1
ttk.Label(frame1, text = "Choose the country:", font = ("Times New Roman", 25), background = 'linen', foreground ="sienna").grid(column = 0,
		row = 1, padx = 10, pady = 25) # создаем виджет для отображения текста
v1 = StringVar() # переменная, содержащая строковые данные
var1 = ttk.Combobox(frame1, width = 20, textvariable = v1, font=("Times New Roman", 20)) # выпадающий список, в котором выбираем страну
var1['values'] = countries # в качестве сроковых данных используем список стран
var1.grid(column = 1, row = 1) # расположение в окне
var1.current()


ttk.Label(frame1, text = "Choose the type of company:", font = ("Times New Roman", 25), background = 'linen',foreground ="sienna").grid(column = 0,
		row = 2, padx = 10, pady = 25)
v2 = StringVar()
var2 = ttk.Combobox(frame1, width = 20, textvariable = v2, font=("Times New Roman", 20)) # выпадающий список, в котором выбираем тип
var2['values'] = types # в качестве сроковых данных используем список типов компаний
var2.grid(column = 1, row = 2)
var2.current()

ttk.Label(frame1, text = "Enter the beginning of the period:\n(in the format dd/mm/yyyy)", font = ("Times New Roman", 25),
          background = 'linen', foreground ="sienna").grid(column = 0, row = 3, padx = 10, pady = 25)
v3 = StringVar()
var3 = Entry(frame1, width = 20, textvariable = v3, font=("Times New Roman", 20)) # поле ввода для получения начала периода
var3.grid(column = 1, row = 3)

ttk.Label(frame1, text = "Enter the end of the period:\n(in the format dd/mm/yyyy)",
		font = ("Times New Roman", 25), background = 'linen', foreground ="sienna").grid(column = 0,
		row = 4, padx = 10, pady = 25)
v4 = StringVar()
var4 = Entry(frame1, width = 20, textvariable = v4, font=("Times New Roman", 20)) # поле ввода для получения конца периода
var4.grid(column = 1, row = 4)
button1 = Button(frame1, text="Draw a graph", font = ("Times New Roman", 25),
                 background="sienna", foreground ='linen', command=clicked1).grid(column = 1, row =5) #кнопка для построения графика по введенным данным

button11 = Button(frame1, text="Information about companies",font = ("Times New Roman", 25), background="sienna", foreground ='linen',
                  command=clicked3).grid(column = 1, row =6) #кнопка для получения информации о компаниях

# frame2
ttk.Label(frame2, text = "Сhoose the first country:", font = ("Times New Roman", 25), background = 'linen', foreground ="sienna").grid(column = 0,
		row = 1, padx = 10, pady = 25)
v10 = StringVar()
var10 = ttk.Combobox(frame2, width = 20, textvariable = v10, font=("Times New Roman", 20)) # выпадающий список, в котором выбираем первую страну
var10['values'] = countries
var10.grid(column = 1, row = 1)
var10.current()

ttk.Label(frame2, text = "Сhoose the second country:", font = ("Times New Roman", 25), background = 'linen', foreground ="sienna").grid(column = 0,
		row = 2, padx = 10, pady = 25)
v11 = StringVar()
var11 = ttk.Combobox(frame2, width = 20, textvariable = v11, font=("Times New Roman", 20)) # выпадающий список, в котором выбираем вторую страну
var11['values'] = countries
var11.grid(column = 1, row = 2)
var11.current()

ttk.Label(frame2, text = "Choose the type of companies:", font = ("Times New Roman", 25), background = 'linen', foreground ="sienna").grid(column = 0,
		row = 3, padx = 10, pady = 25)
v20 = StringVar()
var20 = ttk.Combobox(frame2, width = 20, textvariable = v20, font=("Times New Roman", 20))
var20['values'] = types
var20.grid(column = 1, row = 3)
var20.current()

ttk.Label(frame2, text = "Enter the beginning of the period:\n(in the format dd/mm/yyyy)", font = ("Times New Roman", 25),
          background = 'linen', foreground ="sienna").grid(column = 0, row = 4, padx = 10, pady = 25)
v30 = StringVar()
var30 = Entry(frame2, width = 20, textvariable = v30, font=("Times New Roman", 20))
var30.grid(column = 1, row = 4)

ttk.Label(frame2, text = "Enter the end of the period:\n(in the format dd/mm/yyyy)", font = ("Times New Roman", 25),
          background = 'linen', foreground ="sienna").grid(column = 0, row = 5, padx = 10, pady = 25)
v40 = StringVar()
var40 = Entry(frame2, width = 20, textvariable = v40, font=("Times New Roman", 20))
var40.grid(column = 1, row = 5)
button2 = Button(frame2, text="Построить график",font = ("Times New Roman", 25), background="sienna", foreground ='linen',
                 command=clicked2).grid(column = 1, row =6) #кнопка для построеня двух графиков по введенным данным

note.pack(expand= True, fill=BOTH)
window.mainloop()



