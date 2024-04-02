from sense_emu import SenseHat
import sqlite3

hat = SenseHat()
hat.clear()

class MeteoApp:
    def __init__(self):
        self.current_temperature = 0
        self.current_humidity = 0
        self.current_pressure = 0

    def read_sensor_data_temp(self):
        try:
            self.current_temperature = round(hat.get_temperature(),1)
        except Exception as e:
            print(f"Error reading temperature sensor data: {e}")

    def read_sensor_data_hum(self):
        try:
            self.current_humidity = round(hat.get_humidity())
        except Exception as e:
            print(f"Error reading humidity sensor data: {e}")

    def read_sensor_data_pres(self):
        try:
            self.current_pressure = round(hat.get_pressure())
        except Exception as e:
            print(f"Error reading pressure sensor data: {e}")

    def adjust_values(self):
        try:
            for event in hat.stick.get_events():
                        if event.action == "pressed" and event.direction == "middle":
                            self.save_sensor_data()
                            print("Sensor data saved to database.")
                        elif event.action == "pressed":
                            if event.direction == "up":
                                self.current_temperature += 1
                            elif event.direction == "down":
                                self.current_temperature -= 1
                            elif event.direction == "left":
                                self.current_humidity -= 1
                            elif event.direction == "right":
                                self.current_humidity += 1
            return self.current_temperature, self.current_humidity
        except Exception as e:
            print(f"Error adjusting values: {e}")

    def save_sensor_data(self):
        try:
            conn = sqlite3.connect('database.db')
            cur = conn.cursor()
            cur.execute('''INSERT INTO sensor_data (time, temperature, humidity, pressure)
                        VALUES (CURRENT_TIMESTAMP, ?, ?, ?)''', 
                        (self.current_temperature, self.current_humidity, self.current_pressure))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Error saving sensor data to database: {e}")






    