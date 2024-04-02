from flask import Flask, render_template,redirect, url_for
from services import current_weather_api, daily_weather_api, datetime_services
from services.sensehat import MeteoApp
from models import clothes

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
    current_date_and_time = datetime_services.current_date_and_time()
    clothes_recommendation = clothes.what_to_wear()
    return render_template('index.html', temperature=temperature,
                            humidity= humidity,
                            pressure=pressure, 
                            daily_temp=daily_temp, 
                            daily_hum=daily_hum, 
                            daily_pres=daily_pres, 
                            yesterday_date=yesterday_date,
                            current_date_and_time=current_date_and_time,
                            clothes_recommendation=clothes_recommendation)

# http://www.domena.hr/temppreshum
@app.route('/house')
def temppreshum():
    #current_temperature, current_humidity = adjust_values(current_temperature, current_humidity)
    met = MeteoApp()
    home_temp = met.read_sensor_data_temp()
    home_pres = met.read_sensor_data_pres()
    home_hum = met.read_sensor_data_hum()
    return render_template('house.html',
                            home_temp=home_temp,
                            home_pres=home_pres,
                            home_hum=home_hum)

@app.route('/adjust_values', methods=['POST'])
def adjust_values():
    met = MeteoApp()
    button_adjust = met.adjust_values()
    home_temp = button_adjust[0]
    home_hum = button_adjust[1]
    return redirect(url_for('temppreshum'))

if __name__ == '__main__':
    app.run(debug=True)
