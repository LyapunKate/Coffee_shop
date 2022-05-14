from seller import seller_options
from admin import admin_options
from tkinter import *
import threading


def administrator():
    global  window
    admin = admin_options()
    a_thread = threading.Thread(target=admin.choose_option(window), )
    a_thread.start()

def kassir():
    global window
    seller = seller_options()
    s_thread = threading.Thread(target=seller.choose_option(window), )
    s_thread.start()

for i in range(1, 4):
    global window
    window = Tk()
    window.title("Добро пожаловать в приложение CoffeeShop")
    window.geometry('500x500')
    lbl = Label(window, text="Выберете учётную запись:", font=("Arial Bold", 14))
    lbl.grid(column=0, row=0)
    btn = Button(window, text="Администратор", command=administrator)
    btn.grid(column=0, row=1)
    btn2 = Button(window, text="Кассир", command=kassir)
    btn2.grid(column=0, row=2)
    window.mainloop()
