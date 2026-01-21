import pymysql


class Connection:
    def __init__(self):
        self.conn = None

    def get_connection(self):
        if self.conn is None:
            self.conn = pymysql.connect(
                host="localhost",
                user="root",
                password="menachem")

    def crate_db(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
        cursor.execute("USE mydatabase")
        self.conn.commit()
        cursor.close()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_records
        (id INT AUTO_INCREMENT PRIMARY KEY ,
        timestamp DATETIME ,
        location_name VARCHAR(50),
        country VARCHAR(50) ,
        latitude FLOAT ,
        longitude FLOAT ,
        temperature FLOAT ,
        wind_speed  FLOAT ,
        humidity INT ,
        temperature_category VARCHAR(50),
        wind_category VARCHAR(50))""")
        self.conn.commit()
        cursor.close()



