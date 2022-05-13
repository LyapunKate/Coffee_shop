from DataBase import Data
import threading
lock = threading.RLock()
class admin_options:
    def choose_option(self):
        print('Выберете дальнейшее действие:\n 1. Работники\n 2. Продажи\n 3. Склад\n 4. Закончить работу\n')
        for i in range(1, 5):
            activities = input()
            match activities:
                case 'Работники':
                    self.workers()
                    break
                case 'Продажи':
                    self.purchases()
                    break
                case 'Склад':
                    self.quantity()
                    break
                case 'Закончить работу':
                    self.admin_end_works()
                    break
                case _:
                    print('Неверное действие. Попробуйте ещё раз')

    def workers(self):
        print('')
        self.choose_option()
    def purchases(self):

        global worker_sel_id, product_sel_id
        data = Data()

        print('Выберете фильтр. Если вы не хотите фильтровать по соответствующему полю, напишите 0\n')
        print('Кассир -- \n')
        worker = input()
        if (worker != 0):
            with lock:
                worker_sel_id = data.select('id', 'Sellers', 'sellers.surname = {}'.format(worker))
        print('Продукт -- \n')
        product = input()
        if (product != 0):
            with lock:
                product_sel_id = data.select('id', 'Products', 'ProductName = {}'.format(product))
        print('Начальная дата --\n')
        start_date = input()

        print('Конечная дата --\n')
        end_date = input()
        with lock:
            data.select('*', 'Purchases', 'PearsonID = {} AND ProductID = {} '.format(worker_sel_id, product_sel_id))

        # возможно, тут должен быть вывод
        self.choose_option()


    def quantity(self):
        print('')
        self.choose_option()
    def admin_end_works(self):
        print('Работа успешно завершена')
        return
