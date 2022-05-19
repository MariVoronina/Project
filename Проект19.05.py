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


print(info_stocks("Japan", "Food", "15/02/2020", "05/03/2020"))
#print(info_stocks("Japan", "Food", "05/02/2020", "05/04/2020"))
print(compare_stocks("China", "Japan", "IT", "23/02/2013", "05/12/2019"))
print(company_description("Moskovskiy Kreditnyi Bank OAO"))


from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter import Menu
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker

lst = {'day_number': ['1', '3', '4'], 'orders': [8, 7, 11]}
dframe = pd.DataFrame(lst)
print(dframe)

#time1 = input() #
#time2 = input() #"05/12/2019"
lst = info_stocks("Japan", "Food", "23/02/2019", "05/03/2019")
dframe = pd.DataFrame(lst)
print(dframe)

#lst = info_stocks("Japan", "Food", "15/02/2020", "05/03/2020")
#df = pd.DataFrame(lst)
#plt.plot(df['day_number'], df['orders'])
#print(df)

def clicked3():
    df = pd.DataFrame(info_stocks("Japan", "Food", "23/02/2020", "05/03/2020"),
                      columns=["Ajinomoto Co., Inc.", "House Foods Group Inc"])
    print(df)
    df.plot(y=["Ajinomoto Co., Inc.", "House Foods Group Inc"]).patch.set_facecolor('antiquewhite')
    plt.gcf().canvas.set_window_title("График")  # меняем заголовок
    plt.grid()  # выводим решётку (сетку)
    plt.title('График акций')
    plt.xlabel("Временной промежуток", fontsize=14, fontweight="bold")
    plt.ylabel("Стоимость акции", fontsize=14, fontweight="bold")
    plt.show()






types = ["Banks", "Biotechnology", "Cars", "Hotels", "IT", "Entertainments", "Clothes", "Food"]
countries = ["United States", "Russia", "China", "United Kingdom", "France", "Japan"]

window = Tk()
window.title("Акации по акции")
window.geometry('600x450')
menu = Menu(window)
new_item = Menu(menu)
strana = Menu(new_item)
new_item.add_command(label='График', command=clicked3)
new_item.add_separator()
for i in countries:
    strana.add_command(label=i)
    strana.add_separator()
new_item.add_cascade(label='Сортировать по странам', menu=strana)
new_item.add_separator()
kategoria = Menu(new_item)
for i in types:
    kategoria.add_command(label=i)
    kategoria.add_separator()
new_item.add_cascade(label='Сортировать по категориям', menu=kategoria)
menu.add_cascade(label='Меню', menu=new_item)
window.config(menu=menu)
from PIL import ImageTk, Image
img = Image.open('конор.jpg')
width = 600
ratio = (width / float(img.size[0]))
height = int((float(img.size[1]) * float(ratio)))
imag = img.resize((width, height), Image.ANTIALIAS)
image = ImageTk.PhotoImage(imag)
panel = Label(window, image=image)
panel.pack(side="top", fill="both", expand="no")

window.mainloop()









#df = pd.DataFrame(info_stocks("Japan", "Food", "23/02/2019", "05/12/2019"))
#plt.plot(df['day_number'], df['orders'])
#plt.show()