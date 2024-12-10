import requests
import lookups

def get_data(place, forecast_days=None):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={lookups.API_KEY}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__=='__main__':
    print(get_data(place='Beirut', forecast_days=3, kind='Temperature'))

