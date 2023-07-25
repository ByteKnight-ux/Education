import requests

response = requests.get('https://city.imd.gov.in/citywx/city_weather_test.php?id=42921')
# with open('weather.html', 'w') as f:
#     f.write(response.text)

# raises and error
# print(response.json())

