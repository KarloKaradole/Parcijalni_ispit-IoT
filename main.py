from flask import Flask, render_template
from flask_wtf import FlaskForm

app = Flask(__name__)

# http://www.domena.hr/
@app.route('/')
def index():
    return render_template('index.html')

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
