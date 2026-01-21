from connection import Connection


class Operations:

    @staticmethod
    def insert_to_db(data):
        coon = Connection().conn
        cursor = coon.cursor()
        cursor.execute("USE mydatabase")
        sql = """INSERT INTO  weather_records (
        timestamp,location_name,country,
        latitude,longitude,temperature, wind_speed ,
        humidity, temperature_category,wind_category)
        VALUES (%s, %s,%s, %s, %s, %s ,%s, %s, %s, %s)"""

        for d in data:
            cursor.execute(sql, (d["timestamp"], d["location_name"],
                                d["country"], d["latitude"] ,d["longitude"],
                                 d["temperature"], d["wind_speed"], d["humidity"],
                                 d["temperature_category"], d["wind_category"]))
        coon.commit()
        cursor.close()

    @staticmethod
    def select_all():
        coon = Connection().conn
        cursor = coon.cursor()
        cursor.execute("USE mydatabase")
        sql = """SELECT * FROM weather_records"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            print(i)


o = Operations()
print(o.select_all())
