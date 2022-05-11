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

  def select_workers(self):
      con = psycopg2.connect(
        database='Coffee',
        user='postgres',
        password='VarvaRa14',
        host='localhost',
        port=5432
      )
      cursor = con.cursor()
      cursor.execute("SELECT * FROM SELLERS JOIN ADRESS ON SELLERS.ID = ADRESS.ID")
      # Получаем результат сделанного запро
      results = cursor.fetchall()
      cursor.close()
      return results

  def insert_worker_seller(self, name, surname, middlename):
    con = psycopg2.connect(
      database='Coffee',
      user='postgres',
      password='VarvaRa14',
      host='localhost',
      port=5432
    )
    cursor = con.cursor()
    cursor.execute("INSERT INTO Sellers(Name, Surname, MiddleName) Values ('{}', '{}', '{}')".format(name, surname, middlename))
    # Получаем результат сделанного запро
    con.commit()
    cursor.close()

  def insert_worker_adress(self, id, state, city, street, house):
    con = psycopg2.connect(
      database='Coffee',
      user='postgres',
      password='VarvaRa14',
      host='localhost',
      port=5432
    )
    cursor = con.cursor()
    cursor.execute(
      "INSERT INTO Adress(id, State, City, Street, House) Values ('{}', '{}', '{}', '{}', '{}')".format(id, state, city, street, house))
    # Получаем результат сделанного запро
    con.commit()
    cursor.close()

  def select_worker_id(self, name, surname, middlename):
    con = psycopg2.connect(
      database='Coffee',
      user='postgres',
      password='VarvaRa14',
      host='localhost',
      port=5432
    )
    cursor = con.cursor()
    cursor.execute("SELECT ID FROM SELLERS WHERE Name = {} AND Surname = {} AND MiddleName = {}").format(name, surname, middlename)
    # Получаем результат сделанного запроса
    results = cursor.fetchall()
    for row in results:
      id_result = row[0]
    cursor.close()
    return id_result

  def delete_worker_sellers(self, name, surname, middlename):
    con = psycopg2.connect(
      database='Coffee',
      user='postgres',
      password='VarvaRa14',
      host='localhost',
      port=5432
    )
    cursor = con.cursor()
    cursor.execute(
      "DELETE FROM SELLERS WHERE SELLERS.NAME = {} AND SELLERS.SURNAME = {} AND SELLERS.MIDDLENAME = {}".format(name, surname, middlename))
    # Получаем результат сделанного запроса
    con.commit()
    cursor.close()

  def delete_worker_adress(self, id):
      con = psycopg2.connect(
        database='Coffee',
        user='postgres',
        password='VarvaRa14',
        host='localhost',
        port=5432
      )
      cursor = con.cursor()
      cursor.execute(
        "DELETE FROM ADRESS WHERE ADRESS.ID = {}".format(id))
      # Получаем результат сделанного запроса
      con.commit()
      cursor.close()

  def select_purch(self, what, where, how):
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
    return results

  def select_quantity(self):
      con = psycopg2.connect(
        database='Coffee',
        user='postgres',
        password='VarvaRa14',
        host='localhost',
        port=5432
      )
      cursor = con.cursor()
      cursor.execute("SELECT * FROM QUANTITY")
      # Получаем результат сделанного запроса
      results = cursor.fetchall()
      cursor.close()
      return results

  def select_quantity_prod(self, product):
      con = psycopg2.connect(
        database='Coffee',
        user='postgres',
        password='VarvaRa14',
        host='localhost',
        port=5432
      )
      cursor = con.cursor()
      cursor.execute("SELECT * FROM QUANTITY WHERE QUANTITY.PRODUCT_NAME = {}").format(product)
      # Получаем результат сделанного запроса
      results = cursor.fetchall()
      cursor.close()
      return results

