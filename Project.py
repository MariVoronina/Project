from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter import Menu
def clicked1():
    messagebox.showinfo('Заголовок', 'Здрасте')


def clicked2():
    lbl.configure(text="Я же просил...")


gui = Tk(className='Python Examples - Window Color')
# set window size
gui.geometry("400x200")
#set window color
gui.configure(bg='blue')
gui.mainloop()


types = ["Banks", "Biotechnology", "Cars", "Hotels", "IT", "Entertainments", "Clothes", "Food"]
countries = ["United States", "Russia", "China", "United Kingdom", "France", "Japan"]

window = Tk()
window.title("Акации по акции")
window.geometry('600x450')
menu = Menu(window)
new_item = Menu(menu)
strana = Menu(new_item)
new_item.add_command(label='График', command=clicked1)
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




window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
lbl = Label(window, text="Здарова", font=("Arial Bold", 40))
lbl.grid(column=0, row=0)
btn = Button(window, text="Не нажимать!", command=clicked2)
btn.grid(column=1, row=0)
window.mainloop()


window = Tk()
window.title("Акции крупных фирм")
window.geometry('400x300')

btn = Button(window, text='Клик', command=clicked1)
btn.grid(column=0, row=1)

combo = Combobox(window)
combo['values'] = [btn.grid, 2, 3, 4, 5, "Текст"]
combo.current(1)
combo.grid(column=100, row=0)
window.mainloop()


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
chk_state1 = BooleanVar()
chk_state1.set(True)
chk_state2 = BooleanVar()
chk_state2.set(True)
chk_state3 = BooleanVar()
chk_state3.set(True)
chk1 = Checkbutton(window, text='Пить', var=chk_state1)
chk1.grid(column=0, row=0)
chk2 = Checkbutton(window, text='Или не пить', var=chk_state2)
chk2.grid(column=0, row=1)
chk3 = Checkbutton(window, text='Вот в чем вопрос', var=chk_state3)
chk3.grid(column=0, row=2)
window.mainloop()

window = Tk()
window.title("Акации по акции")
window.geometry('400x250')
rad1 = Radiobutton(window, text='Первый', value=1)
rad2 = Radiobutton(window, text='Второй', value=2)
rad3 = Radiobutton(window, text='Третий', value=3)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
window.mainloop()


def clicked():
    lbl.configure(text=selected.get())


window = Tk()
window.title("Акции")
window.geometry('400x300')
selected = IntVar()
rad1 = Radiobutton(window, text='1', value=1, variable=selected)
rad2 = Radiobutton(window, text='2', value=2, variable=selected)
rad3 = Radiobutton(window, text='3', value=3, variable=selected)
btn = Button(window, text="Клик", command=clicked)
lbl = Label(window)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn.grid(column=3, row=0)
lbl.grid(column=0, row=1)
window.mainloop()




