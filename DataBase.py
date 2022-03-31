import psycopg2 as psycopg2

class Data:
#pip3 install psycopg2
  def connect(self):
    con = psycopg2.connect(
      database='Coffee',
      user='postgres',
      password='VarvaRa14',
      host='localhost',
      port=5432
    )
    return con

  def select(self, what, where, how):
    cursor = self.connect.cursor()
    cursor.execute("SELECT {} FROM {} WHERE {}".format(what, where, how))
# Получаем результат сделанного запрос
    results = cursor.fetchall()
    print(results)
    self.connect.close()

  def begin_work(self, who, start_date):
    cursor = self.connect.cursor()
    cursor.execute("INSERT INTO work(surname, start_date) Values ({}, '{}')".format(who, start_date))
# Получаем результат сделанного запро
    self.connect.commit()
    self.connect.close()

  def end_work(self, who, end_date):
    cursor = self.connect.cursor()
    cursor.execute("INSERT INTO work(end_date) Values ('{}') where surname = {} and end_date IS NULL".format(end_date, who))
    # Получаем результат сделанного запро
    self.connect.commit()
    self.connect.close()

  def insert(self, id, quantity, time):
    cursor = self.connect.cursor()
    cursor.execute("INSERT INTO purchases(ProductID, Quantity, DateTime) Values ({}, '{}', '{}')".format(id, quantity, time))
    # Получаем результат сделанного запро
    self.connect.commit()
    self.connect.close()

  def select_time(self):
    cursor = self.connect.cursor()
    cursor.execute("SELECT NOW()")
# Получаем результат сделанного запрос
    results = cursor.fetchall()
    self.connect.close()
    return results


# [('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',), ('Aaron Goldberg',)]
#