import requests
api_add = 'http://api.openweathermap.org/data/2.5/weather?appid=338acd0be4d51bba42999365b245dcf6&q='
city = input("City name : ")

url = api_add + city


r = requests.get(url).json()
get_city_weather = r.[]

print(r)

