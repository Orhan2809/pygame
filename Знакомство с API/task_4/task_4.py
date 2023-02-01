from requests import get
from os import environ

API_KEY = environ["YANDEX_MAPS_API_KEY"]
city = ["Барнаул", "Мелеуз", "Йошкар-Ола"]
response = get(f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode=Петровки, 38,&format=json")
response_json = response.json()
print(response_json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]
      ["GeocoderMetaData"]["Address"]["postal_code"])
