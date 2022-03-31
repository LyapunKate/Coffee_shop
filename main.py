from seller import seller_options
from admin import admin_options
for i in range(1, 4):
    print('Выберете учётную запись:\n 1. администратор\n 2. кассир ')
    pearsontype = input()
    match pearsontype:
        case 'администратор':
            admin = admin_options()
            admin.choose_option()
        case 'кассир':
            seller = seller_options()
            seller.choose_option()
        case _:
            print('Неверная учётная запись. Попробуйте ещё раз')

