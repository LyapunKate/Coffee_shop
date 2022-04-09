import psycopg2 as psycopg2

class Data:

  def select(self, what, where, how):
    global select_result
    con = psycopg2.connect(
      database='Coffee',
      user='postgres',
      password='VarvaRa14',
      host='localhost',
      port=5432
    )
    cursor = con.cursor()
    cursor.execute("SELECT {} FROM {} WHERE {}".format(what, where, how))
# Получаем результат сделанного запрос
    results = cursor.fetchall()
    for row in results:
      select_result = row[0]
    cursor.close()
    return select_result

  def begin_work(self, who, start_date):
    con = psycopg2.connect(
      database='Coffee',
      user='postgres',
      password='VarvaRa14',
      host='localhost',
      port=5432
    )
    cursor = con.cursor()
    cursor.execute("INSERT INTO Work(surname, start_date) Values ({}, '{}')".format(who, start_date))
# Получаем результат сделанного запро
    con.commit()
    cursor.close()

  def end_work(self, who, end_date):
    con = psycopg2.connect(
      database='Coffee',
      user='postgres',
      password='VarvaRa14',
      host='localhost',
      port=5432
    )
    cursor = con.cursor()
    cursor.execute("UPDATE Work SET end_date = '{}' where surname = {} and end_date IS NULL".format(end_date, who))
    # Получаем результат сделанного запро
    con.commit()
    cursor.close()

  def insert(self, id, quantity, time):
    con = psycopg2.connect(
      database='Coffee',
      user='postgres',
      password='VarvaRa14',
      host='localhost',
      port=5432
    )
    cursor = con.cursor()
    cursor.execute("INSERT INTO purchases(ProductID, Quantity, DateTime) Values ({}, {}, '{}')".format(id, quantity, time))
    # Получаем результат сделанного запро
    con.commit()
    cursor.close()

  def select_time(self):
    global time_result
    con = psycopg2.connect(
      database='Coffee',
      user='postgres',
      password='VarvaRa14',
      host='localhost',
      port=5432
    )
    cursor = con.cursor()
    cursor.execute("SELECT NOW()")
# Получаем результат сделанного запрос
    results = cursor.fetchall()
    for row in results:
      time_result = row[0]
    cursor.close()
    return time_result

