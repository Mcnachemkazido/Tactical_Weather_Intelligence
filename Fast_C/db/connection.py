import pymysql
from dotenv import load_dotenv
import os

load_dotenv()
DB_HOST = os.getenv("DB_HOST")

class Connection:
    def __init__(self):
        self.conn = pymysql.connect(
            host= DB_HOST,
            user= "root",
            password= "menachem"
        )

        self.create_db()
        self.create_table()

    def create_db(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
        self.conn.select_db('mydatabase')
        cursor.close()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_records (
            id INT AUTO_INCREMENT PRIMARY KEY,
            timestamp DATETIME,
            location_name VARCHAR(50),
            country VARCHAR(50),
            latitude FLOAT,
            longitude FLOAT,
            temperature FLOAT,
            wind_speed FLOAT,
            humidity INT,
            temperature_category VARCHAR(50),
            wind_category VARCHAR(50)
        )""")
        self.conn.commit()
        cursor.close()