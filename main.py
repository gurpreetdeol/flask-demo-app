from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)
FLASK_APP = app
FLASK_ENV = 'development'
FLASK_DEBUG = 'true'

date_format = "%Y-%m-%d %H:%M:%S"
india_timezone = pytz.timezone('Asia/Kolkata')
datetime_india = datetime.now(india_timezone)

toronto_timezone = pytz.timezone('Canada/Eastern')
vancouver_timezone = pytz.timezone('Canada/Pacific')


@app.route('/')
def home():
    return (f"India Time: {datetime_india.strftime(date_format)} "
            f"Toronto Time: {datetime.now(toronto_timezone).strftime(date_format)} "
            f"Vancouver Time: {datetime.now(vancouver_timezone).strftime(date_format)}")


if __name__ == "__main__":
    app.run(debug=True)
