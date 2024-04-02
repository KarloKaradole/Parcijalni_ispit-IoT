import sqlite3
import os

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect(os.path.join('database', 'sensor_data.db'))
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS sensor_data (
                            id INTEGER PRIMARY KEY,
                            timestamp TEXT NOT NULL,
                            temperature REAL NOT NULL,
                            humidity REAL NOT NULL,
                            pressure REAL NOT NULL
                        )''')
        self.conn.commit()

    def save_sensor_data(self, timestamp, temperature, humidity, pressure):
        self.cur.execute('''INSERT INTO sensor_data (timestamp, temperature, humidity, pressure) 
                            VALUES (?, ?, ?, ?)''', (timestamp, temperature, humidity, pressure))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
