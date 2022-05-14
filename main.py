from seller import seller_options
from admin import admin_options
from tkinter import *
import threading


def administrator():
    admin = admin_options()
    a_thread = threading.Thread(target=admin.choose_option(), )
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


    # print('Выберете учётную запись:\n 1. администратор\n 2. кассир ')
    #pearsontype = input()
    #match pearsontype:
    #    case 'администратор':
    #        admin = admin_options()
    #        admin.choose_option()
    #    case 'кассир':
    #        seller = seller_options()
    #        end = seller.choose_option()
    #        if end == 'end':
    #            exit(0)
    #    case _:
    #        print('Неверная учётная запись. Попробуйте ещё раз')

