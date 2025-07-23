#this will take weather data and return a risk score

#---------------- Funciton -------------------
# Purpose: to calculate the risk of harvesting 
# based on data
# Input: data from getWeather
# Output: risk meter number
#---------------------------------------------


def calcHarvestRisk(forecast_list):
    if not forecast_list:
        return {'error': 'No forecast data available'}

    temps = [f['temp'] for f in forecast_list if f.get('temp') is not None]
    winds = [f['wind'] for f in forecast_list if f.get('wind') is not None]
    humids = [f['humidity'] for f in forecast_list if f.get('humidity') is not None]

    if not temps or not winds or not humids:
        return {'error': 'Incomplete forecast data'}

    max_temp = max(temps)
    max_wind = max(winds)
    max_humidity = max(humids)

    risks ={
        'safe' : 'SAFE TO HARVEST',
        'moderate' : 'MODERATE RISK',
        'high' : 'HIGH RISK'
    }

    if max_temp >= 100 and max_wind >= 15:
        return {
            'risk_level': 'high',
            'message': risks['high'],
            'max_temp': max_temp,
            'max_wind': max_wind,
            'max_humidity': max_humidity
        }
    elif max_temp >= 100 or max_wind >= 15 or max_humidity >= 50:
        return {
            'risk_level': 'moderate',
            'message': risks['moderate'],
            'max_temp': max_temp,
            'max_wind': max_wind,
            'max_humidity': max_humidity
        }
    else:
        return {
            'risk_level': 'safe',
            'message': risks['safe'],
            'max_temp': max_temp,
            'max_wind': max_wind,
            'max_humidity': max_humidity
        }
