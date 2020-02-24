import pygame
import requests


def get_mapimg(static_par):
    response = requests.get(static_server, params=static_par)

    # if response:
    #     return pygame.image.frombuffer(response.content, (450, 450), "RGB")
    # return None

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return pygame.image.load(map_file)


static_server = "https://static-maps.yandex.ru/1.x/?"
static_params = {"l": 'map',
                 "ll": "37.620070,55.753630"}
geocoder_server = "https://geocode-maps.yandex.ru/1.x/?"
geocoder_params = {"apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                   "geocode": None}

static_params["z"] = input("введите масштаб(0-17):")
static_params["ll"] = input("долгота и широта ч/з запятую:")

pygame.init()
size = WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode(size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    screen.blit(get_mapimg(static_params), (0, 0))

    pygame.display.flip()
