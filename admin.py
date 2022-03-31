from DataBase import Data

class admin_options:
    def choose_option(self):
        print('Выберете дальнейшее действие:\n 1. Работники\n 2. Продажи\n 3. Склад\n')
        for i in range(1, 4):
            activities = input()
            match activities:
                case 'Работники':
                    self.workers()
                case 'Продажи':
                    self.purchases()
                case 'Склад':
                    self.quantity()
                case _:
                    print('Неверное действие. Попробуйте ещё раз')

    def workers(self):
        print('')
    def purchases(self):
        global worker_sel_id, product_sel_id
        data = Data()

        print('Выберете фильтр. Если вы не хотите фильтровать по соответствующему полю, напишите 0\n')
        print('Кассир -- \n')
        worker = input()
        if (worker != 0):
            worker_sel_id = data.select('id', 'Sellers', 'sellers.surname = {}'.format(worker))
        print('Продукт -- \n')
        product = input()
        if (product != 0):
            product_sel_id = data.select('id', 'Products', 'ProductName = {}'.format(product))
        print('Начальная дата --\n')
        start_date = input()

        print('Конечная дата --\n')
        end_date = input()
        data.select('*', 'Purchases', 'PearsonID = {} AND ProductID = {} '.format(worker_sel_id, product_sel_id))
    def quantity(self):
        print('')

