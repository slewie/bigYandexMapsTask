import os
import sys
from math import sqrt
import pygame
import requests


x, y = 0, 0
w, h = 0, 0
def_l = 'map'
def_spn = '0.15,0.10'
def_ll = '30.25,59.947176'
n = 0


def draw_text_find(screen, text):
    global x, y, w, h
    font1 = pygame.font.Font(None, 50)
    text = font1.render(text, 1, (100, 255, 100))
    text_x = 600 - text.get_width() - 10 - 30
    text_y = 450 - text.get_height() - 10
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)
    x, y, w, h = text_x, text_y, text_w, text_h


def get_request(l=def_l, spn=def_spn, ll=def_ll):
    global def_ll, def_spn, def_l
    response = None
    server = 'https://static-maps.yandex.ru/1.x/'
    params = {
        'l': l,
        'spn': spn,
        'll': ll,
        'pt': f'{ll},pm2bll'
    }
    response = requests.get(server, params=params)
    def_l = l
    def_spn = spn
    def_ll = ll
    return response


def write_image():
    global response, map_file
    with open(map_file, "wb") as file:
        file.write(response.content)


def draw_image():
    global screen
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()


def draw_text_input():
    global input_box, color, text
    font = pygame.font.Font(None, 32)
    txt_surface = font.render(text, True, color)
    width = max(200, txt_surface.get_width() + 10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, color, input_box, 2)
    pygame.display.flip()


def draw():
    global screen
    screen.fill((0, 0, 0))
    draw_image()
    draw_text_find(screen, 'Искать')
    draw_text_input()


def search_coord(text):
    if text != '':
        server = 'https://geocode-maps.yandex.ru/1.x/'
        params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            'geocode': text,
            'format': 'json'
        }
        resp = requests.get(server, params=params).json()
        if resp['response']['GeoObjectCollection']['featureMember'] != []:
            address_ll = resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
            address_ll = ','.join(i for i in address_ll.split(' '))
            return address_ll
        return 0
    return 0


response = get_request()
map_file = "map.png"
write_image()

pygame.init()
screen = pygame.display.set_mode((600, 450))
clock = pygame.time.Clock()
input_box = pygame.Rect(400, 418 - 55, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''

go = ''
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x1, y1 = event.pos
                if x1 in range(x, x + w) and y1 in range(y, y + h):
                    ll = search_coord(text)
                    if ll != 0:
                        response = get_request(ll=ll)
                        write_image()
                    text = ''
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    ll = search_coord(text)
                    if ll != 0:
                        response = get_request(ll=ll)
                        write_image()
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
    draw()
    clock.tick(10)


pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)