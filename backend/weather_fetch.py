#just contains logic to call the weather API
import requests
import os
from dotenv import load_dotenv

load_dotenv()

#---------------- Funciton -------------------
# Purpose: 
# Input: 
# Output:
#---------------------------------------------

#---------------- getWeather -------------------
# Purpose: makes a request to OpenWeatherMap's 
# forecast API 
# Input: Zipcode
# Output: list of dictionaries with time, 
# temp, wind, humidity and rainfall
#-----------------------------------------------
def getWeather(zipcode):
    API_KEY = os.environ.get('WEATHER_API_KEY')
    if not API_KEY:
        raise Exception("EXCEPTION - missing api key in environment variables")

    url = "https://api.openweathermap.org/data/2.5/forecast"
    parameters = {
        'zip' : f'{zipcode},us',
        'appid' : API_KEY,
        'units' : 'imperial'
    }

    response = requests.get(url, params=parameters)

    if response.status_code == 200:
        data = response.json()
        #print("Current temperature:", data["main"]["temp"], "°F")
    else:
        raise Exception(f"Weather API Error {response.status_code}: {response.text}")

    data = response.json()
    simplified_forecast = []

    #TODO: loop through data list and pull out datetime, temp, humidity, rainfall
    for entry in data['list'][:5]:
        forecast = {
            'time' : entry['dt_txt'],
            'temp' : entry['main']['temp'],
            'wind' : entry['wind']['speed'],
            'humidity' : entry['main']['humidity'],
            'rain' : entry.get('rain', {}).get('3h', 0),
        }
        simplified_forecast.append(forecast)
    print("Simplified forecast: ", simplified_forecast)
    return simplified_forecast

if __name__ == "__main__":
            zip_code = "99324"
            forecast = getWeather(zip_code)
            for f in forecast:
                print(f)