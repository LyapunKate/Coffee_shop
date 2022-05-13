from client import seller_options
from admin import admin_options
import threading

for i in range(1, 4):
    print('Выберете учётную запись:\n 1. администратор\n 2. кассир ')
    pearsontype = input()
    match pearsontype:
        case 'администратор':
            admin = admin_options()
            a_thread = threading.Thread(target= admin.choose_option(), )
            a_thread.start()
        case 'кассир':
            seller = seller_options()
            s_thread = threading.Thread(target= seller.choose_option(), )
            s_thread.start()
        case _:
            print('Неверная учётная запись. Попробуйте ещё раз')
