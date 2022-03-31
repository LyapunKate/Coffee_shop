from DataBase import Data

class seller_options:
        def choose_option(self):
            print('Выберете дальнейшее действие:\n 1. Начать смену\n 2. Продать\n 3. Завершить смену\n')
            data = Data()
            for i in range(1, 3):
                activities = input()
                match activities:
                    case 'Начать смену':
                        print ('Введите фамилию\n')
                        surname = input()
                        print ('Введите дату и время начало\n')
                        start_date = input()
                        data.begin_work(surname, start_date)
                    case 'Продать':
                        print ('Введите название продукта\n')
                        product = input()
                        product_sel_id = data.select('id', 'Products', 'ProductName = {}'.format(product))
                        print ('Введите количество\n')
                        quantity = input()
                        time = data.select_time()
                        data.insert(product_sel_id, quantity, time)

                    case 'Закончить смену':
                        print ('Введите фамилию\n')
                        surname = input()
                        print ('Введите дату и время начало\n')
                        end_date = input()
                        data.end_work(surname, end_date)
                    case _:
                        print('Неверное действие. Попробуйте ещё раз')