import mysql.connector

conn = None

try:
    conn = mysql.connector.connect(host='localhost', 
                                   port=3306,
                                   database='weather_db',
                                   user='matti',
                                   password='my_password')
    if conn.is_connected():
        print('Connected to MySQL database')

except mysql.connector.Error as e:
    print(e)

finally:
    if conn is not None and conn.is_connected():
        conn.close()

def create_db():
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE  IF NOT EXISTS weather_db")
    
