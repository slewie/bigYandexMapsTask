import os
import sys
from math import sqrt
import pygame
import requests

response = None
server = 'https://static-maps.yandex.ru/1.x/'
params = {
    'l': 'map',
    'spn': '0.2,0.2',
    'll': '30.25,59.947176'
}
response = requests.get(server, params=params)

pos = [30.25, 59.947176]

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)


pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pos[1] += 0.28
                params['ll'] = ','.join(str(i) for i in pos)
                response = requests.get(server, params=params)
                with open(map_file, "wb") as file:
                    file.write(response.content)
                screen.fill((0, 0, 0))
                screen.blit(pygame.image.load(map_file), (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_DOWN:
                pos[1] -= 0.28
                params['ll'] = ','.join(str(i) for i in pos)
                response = requests.get(server, params=params)
                with open(map_file, "wb") as file:
                    file.write(response.content)
                screen.fill((0, 0, 0))
                screen.blit(pygame.image.load(map_file), (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_LEFT:
                pos[0] -= 0.6
                params['ll'] = ','.join(str(i) for i in pos)
                response = requests.get(server, params=params)
                with open(map_file, "wb") as file:
                    file.write(response.content)
                screen.fill((0, 0, 0))
                screen.blit(pygame.image.load(map_file), (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_RIGHT:
                pos[0] += 0.6
                params['ll'] = ','.join(str(i) for i in pos)
                response = requests.get(server, params=params)
                with open(map_file, "wb") as file:
                    file.write(response.content)
                screen.fill((0, 0, 0))
                screen.blit(pygame.image.load(map_file), (0, 0))
                pygame.display.flip()
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)