from flask import Flask, render_template
from services import current_weather_api, daily_weather_api, datetime_services

app = Flask(__name__)

# http://www.domena.hr/
@app.route('/')
def index():
    temperature = current_weather_api.weather_temperature()
    humidity = current_weather_api.weather_humidity()
    pressure = current_weather_api.weather_pressure()
    daily_temp = daily_weather_api.daily_temperature()
    daily_hum = daily_weather_api.daily_humidity()
    daily_pres = daily_weather_api.daily_pressure()
    yesterday_date = datetime_services.get_yesterday_datetime()
    return render_template('index.html', temperature=temperature, humidity= humidity, pressure=pressure, daily_temp=daily_temp, daily_hum=daily_hum, daily_pres=daily_pres, yesterday_date=yesterday_date)

# http://www.domena.hr/temperature
@app.route('/temperature')
def temperature():
    return render_template('temperature.html')

# http://www.domena.hr/pressure
@app.route('/pressure')
def pressure():
    return render_template('pressure.html')

# http://www.domena.hr/humidity
@app.route('/humidity')
def humidity():
    return render_template('humidity.html')


if __name__ == '__main__':
    app.run(debug=True)
