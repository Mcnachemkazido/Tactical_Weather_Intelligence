from db.connection import Connection


class Operations:

    @staticmethod
    def insert_to_db(data):
        connection = Connection()
        conn = connection.conn
        cursor = conn.cursor()

        sql = """INSERT INTO weather_records (
            timestamp, location_name, country,
            latitude, longitude, temperature, wind_speed,
            humidity, temperature_category, wind_category)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        for d in data:
            cursor.execute(sql, (
                d["timestamp"], d["location_name"], d["country"],
                d["latitude"], d["longitude"], d["temperature"],
                d["wind_speed"], d["humidity"], d["temperature_category"],
                d["wind_category"]
            ))

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def select_all():
        connection = Connection()
        conn = connection.conn
        cursor = conn.cursor()

        sql = """SELECT * FROM weather_records"""
        cursor.execute(sql)
        result = cursor.fetchall()

        cursor.close()
        conn.close()
        return result