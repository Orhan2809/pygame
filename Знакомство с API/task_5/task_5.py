import os
from os import environ
import pygame
from requests import get
running = True
API_KEY = environ["YANDEX_MAPS_API_KEY"]
pos = get(f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode=Австралия&format=json")
position = pos.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]['pos']
response = get(f"http://static-maps.yandex.ru/1.x/?ll={position.split()[0]},{position.split()[1]}&spn=18,18&l=map")
map_image = "map.png"
with open(map_image, "wb") as file:
    file.write(response.content)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    image = pygame.image.load(map_image)
    screen.blit(image, (0, 0))
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
    os.remove(map_image)