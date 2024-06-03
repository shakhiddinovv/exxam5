import psycopg2
import threading
import time
import requests

#1-masala
# conn = psycopg2.connect(
#     host="localhost",
#     database="n42",
#     user="postgres",
#     password="123"
# )

# cur = conn.cursor()

# cur.execute("""
#     CREATE TABLE Product (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(100),
#         price DECIMAL(10,2),
#         color VARCHAR(50),
#         image VARCHAR(200)
#     )
# """)
# conn.commit()
# 2-masala
# def insert_product(name, price, color, image):
#     cur.execute("""
#         INSERT INTO Product (name, price, color, image)
#         VALUES (%s, %s, %s, %s)
#     """, (name, price, color, image))
#     conn.commit()

# def select_all_products():
#     cur.execute("SELECT * FROM Product")
#     return cur.fetchall()

# def update_product(id, name, price, color, image):
#     cur.execute("""
#         UPDATE Product
#         SET name=%s, price=%s, color=%s, image=%s
#         WHERE id=%s
#     """, (name, price, color, image, id))
#     conn.commit()

# def delete_product(id):
#     cur.execute("DELETE FROM Product WHERE id=%s", (id,))
#     conn.commit()

#5-masala
# def save(self):
#         cur.execute("""
#             INSERT INTO Product (name, price, color, image)
#             VALUES (%s, %s, %s, %s)
#         """, (self.name, self.price, self.color, self.image))
#         conn.commit()


#3-masala
# class Alphabet:
#     def __init__(self):
#         self.letters = [chr(ord('A') + i) for i in range(26)] 

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index >= len(self.letters): 
#             raise StopIteration
#         letter = self.letters[self.index]  
#         self.index += 1 
#         return letter

# alphabet = Alphabet()
# for letter in alphabet:
#     print(letter)

#4-masala

# def print_numbers():
#     for i in range(1, 5):
#         print(i)
#         time.sleep(1)

# def print_letters():
#     letters = "ABCDE"
#     for letter in letters:
#         print(letter)
#         time.sleep(1)

# t1 = threading.Thread(target=print_numbers)
# t2 = threading.Thread(target=print_letters)

# t1.start()
# t2.start()
# t1.join()
# t2.join()

#6-masala
# class DbConnect:
#     def __init__(self, database, user, password, host, port):
#         host = 'localhost'
#         user = 'postgres'
#         password = '123'
#         database = 'n42'
#         port = 5432
#         conn = psycopg2.connect(host=host,
#                         database=database,
#                         user=user,
#                         password=password,
#                         port=port
#                         )
#         cur = conn.cursor()

#     def __enter__(self):
#         self.conn = psycopg2.connect(database=self.database, user=self.user, password=self.password, host=self.host, port=self.port)
#         self.cur = self.conn.cursor()
#         return self.conn, self.cur

#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.cur:
#             self.cur.close()
#         if self.conn:
#             self.conn.close()

# with DbConnect(database="n42", user="postgres", password=123, host="localhost", port=5432) as (conn, cur):
#     cur.execute("SELECT * FROM table")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)

#7-masala

object = requests.get('https://dummyjson.com/products/')

