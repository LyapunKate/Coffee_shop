from DataBase import Data

import threading
lock = threading.RLock()
isnt_start = True
class seller_options:

    def choose_option(self):
        for i in range(1, 3):
            global isnt_start
            if isnt_start:
                print('Войдите в систему\n')
                isnt_start = False
                self.seller_begin_work()
                break
            print('Выберете дальнейшее действие:\n 1. Продать\n 2. Закончить смену\n')
            activities = input()
            match activities:
                case 'Продать':
                    end = self.seller_sell()
                    break

                case 'Закончить смену':
                    end = self.seller_end_work()
                    break

                case _:
                    print('Неверное действие. Попробуйте ещё раз')

    def seller_begin_work(self):
        data = Data()
        print('Введите фамилию\n')
        surname = input()
        with lock:
            start_date = data.select_time()
            data.begin_work(surname, start_date)
        self.choose_option()

    def seller_sell(self):
        data = Data()
        print('Введите название продукта\n')
        product = input()
        with lock:
            product_sel_id = data.select('id', 'Products', 'ProductName = {}'.format(product))
        print('Введите количество\n')
        quantity = input()
        with lock:
            time = data.select_time()
            data.insert(product_sel_id, quantity, time)
        print('Покупка успешно проведена\n')
        self.choose_option()

    def seller_end_work(self):
        data = Data()
        print('Введите фамилию\n')
        surname = input()
        with lock:
            end_date = data.select_time()
            data.end_work(surname, end_date)
        print('Работа успешно завершена')
        return
