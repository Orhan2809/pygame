from requests import get
from os import environ

API_KEY = environ["YANDEX_MAPS_API_KEY"]
city = ["Хабаровск", "Нижний Новгород", "Калининград", "Уфа"]
for i in range(len(city)):
    response = get(f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={city[i]},&format=json")
    response_json = response.json()
    print(response_json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]
          ["GeocoderMetaData"]["Address"]["Components"][1]["name"], "-", city[i])