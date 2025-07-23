#runs the flask server and handles HTTP requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from weather_fetch import getWeather
from risk_calc import calcHarvestRisk
from dotenv import load_dotenv
import os

load_dotenv()

#---------------- Funciton -------------------
# Purpose: gather the input needed for the 
# api request
# Input: user input
# Output: zipcode
#---------------------------------------------

app = Flask(__name__)
CORS(app)

@app.route('/harvest-risk')
def harvest_risk():
    zipcode = request.args.get('zip')

    if not zipcode or not zipcode.isdigit() or len(zipcode) != 5:
        return jsonify({'error': 'Invalid ZIP code format. Please enter a 5-digit ZIP code.'}), 400

    try:
        forecast = getWeather(zipcode)
        risk_report = calcHarvestRisk(forecast)
        return jsonify(risk_report)
    except Exception as e:
        return jsonify({'error' : str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

