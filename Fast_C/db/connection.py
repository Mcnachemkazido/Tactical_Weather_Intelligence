import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="menachem"
)




cursor = mydb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
cursor.execute("USE mydatabase")

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


# cursor.execute("SHOW TABLES")
#
# for x in cursor:
#   print(x)