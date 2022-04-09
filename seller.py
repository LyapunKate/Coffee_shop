from DataBase import Data

class seller_options:

        def choose_option(self):
            global end
            end = 'begin'
            for i in range(1, 3):
                print('Выберете дальнейшее действие:\n 1. Начать смену\n 2. Продать\n 3. Закончить смену\n')
                activities = input()
                match activities:
                    case 'Начать смену':

                        end = self.seller_begin_work()
                        break


                    case 'Продать':
                        end = self.seller_sell()
                        break

                    case 'Закончить смену':
                        end = self.seller_end_work()
                        break

                    case _:
                        print('Неверное действие. Попробуйте ещё раз')

            return end

        def seller_begin_work(self):
            global end
            data = Data()
            print('Введите фамилию\n')
            surname = input()
            start_date = data.select_time()
            data.begin_work(surname, start_date)
            print('Выберете дальнейшее действие:\n 1. Продать\n 2. Закончить смену\n')
            activities = input()
            match activities:
                case 'Продать':
                    self.seller_sell()
                case 'Закончить смену':
                    end = self.seller_end_work()
            return end

        def seller_sell(self):
            global end
            data = Data()
            print('Введите название продукта\n')
            product = input()
            product_sel_id = data.select('id', 'Products', 'ProductName = {}'.format(product))
            print('Введите количество\n')
            quantity = input()
            time = data.select_time()
            data.insert(product_sel_id, quantity, time)
            print('Покупка успешно проведена\n')
            print('Если хотите закончить введите END\n')
            print('Если хотите продолжить введите C\n')
            next = input()
            match next:
                case 'C':
                    self.seller_sell()
                case 'END':
                    end = self.seller_end_work()
            return end


        def seller_end_work(self):
            global end
            data = Data()
            print('Введите фамилию\n')
            surname = input()
            end_date = data.select_time()
            data.end_work(surname, end_date)
            print('Работа успешно завершена')
            end = 'end'
            return end
