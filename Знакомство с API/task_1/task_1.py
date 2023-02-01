from os import environ
import requests
API_KEY = environ["YANDEX_MAPS_API_KEY"]
response = requests.get(
    f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode=Москва,Красная площадь,1&format=json")
json_response = response.json()
print(json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
          "GeocoderMetaData"]["Address"]["formatted"].replace(",", ""),
      json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"])
