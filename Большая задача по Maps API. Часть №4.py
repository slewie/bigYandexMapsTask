import os
import sys
from math import sqrt
import pygame
import requests


x, y = 0, 0
w, h = 0, 0


def draw(screen, text):
    global x, y, w, h
    font = pygame.font.Font(None, 50)
    text = font.render(text, 1, (100, 255, 100))
    text_x = 600 // 2 - text.get_width() // 2
    text_y = 450 // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)
    x, y, w, h = text_x, text_y, text_w, text_h


response = None
server = 'https://static-maps.yandex.ru/1.x/'
params = {
    'l': 'map',
    'spn': '0.15,0.10',
    'll': '30.25,59.947176'
}
response = requests.get(server, params=params)

size = 0.1

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)


lst = ['map', 'sat', 'skl']
n = 0

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
draw(screen, lst[n])
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x1, y1 = event.pos
                if x1 in range(x, x + w) and y1 in range(y, y + h):
                    n += 1
                    if n > 2:
                        n = 0
                    params['l'] = lst[n]
                    response = requests.get(server, params=params)
                    with open(map_file, "wb") as file:
                        file.write(response.content)
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.image.load(map_file), (0, 0))
                    draw(screen, lst[n])
                    pygame.display.flip()


pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)