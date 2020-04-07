import requests
import pygame
import os

x, y = 0, 0
w, h = 0, 0
def_l = 'map'
def_spn = '0.01,0.01'
def_ll = '30.25,59.947176'
def_pt = '30.25,59.947176'
lst = ['map', 'sat', 'skl']
n = 0
address = ''
size = 0.01
mp = False
index_status = False
index = ' '
sz_lst = [0.01, 0.1, 0.9, 1.8]
size_lst = [[0.013, 0.00545], [0.21, 0.0865], [1.65, 0.685], [3.3, 1.37]]
mashtab_lst = [0.002, 0.025, 0.1, 0.2]
s = 0
dr = False


def draw_button_reset(screen, text):
    global box_reset
    font1 = pygame.font.Font(None, 50)
    text = font1.render(text, 1, (0, 0, 255))
    text_x = 10
    text_y = 10
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 0, 255), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)
    box_reset = pygame.Rect(text_x - 10, text_y - 10,
                           text_w + 20, text_h + 20)


def draw_text_find(screen, text):
    global input_box2
    font1 = pygame.font.Font(None, 50)
    text = font1.render(text, 1, (0, 0, 255))
    text_x = 600 - text.get_width() - 10 - 30
    text_y = 450 - text.get_height() - 10
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 0, 255), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)
    input_box2 = pygame.Rect(text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20)


def draw_button_switch(screen, text):
    global input_box3
    font1 = pygame.font.Font(None, 50)
    text = font1.render(text, 1, (0, 0, 255))
    text_x = 10
    text_y = 450 - text.get_height() - 10
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 0, 255), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)
    input_box3 = pygame.Rect(text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20)


def address_text(screen, text):
    font1 = pygame.font.Font(None, 15)
    text = font1.render(text, 1, (0, 0, 255))
    text_x = 100
    text_y = 10
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))


def draw_text_for_index_box(screen, text):
    font1 = pygame.font.Font(None, 18)
    text = font1.render(text, 1, (0, 0, 255))
    text_x = 325
    text_y = 410
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))


def draw_box_index(screen):
    global index_status, box_index
    x, y, w, h = 300, 400, 20, 20
    if index_status:
        pygame.draw.rect(screen, (0, 0, 255), (x, y, w, h))
    else:
        pygame.draw.rect(screen, (0, 0, 255), (x, y, w, h), 3)
    box_index = pygame.Rect(x, y, w, h)


def draw_button_plus(screen, text):
    global box_plus
    font1 = pygame.font.Font(None, 50)
    text = font1.render(text, 1, (0, 0, 255))
    text_x = 600 - text.get_width() - 10
    text_y = 10
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 0, 255), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)
    box_plus = pygame.Rect(text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20)


def draw_button_minus(screen, text):
    global box_minus
    font1 = pygame.font.Font(None, 50)
    text = font1.render(text, 1, (0, 0, 255))
    text_x = 600 - text.get_width() - 15
    text_y = 10 + text.get_height() + 20
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 0, 255), (560, text_y - 10,
                                           40, text_h + 20), 1)
    box_minus = pygame.Rect(560, text_y - 10,
                                           40, text_h + 20)


def get_request(l=def_l, spn=def_spn, ll=def_ll, pt=def_pt):
    global def_ll, def_spn, def_l, def_pt
    response = None
    server = 'https://static-maps.yandex.ru/1.x/'
    params = {
        'l': l,
        'spn': spn,
        'll': ll,
        'pt': f'{pt},pm2bll'
    }
    response = requests.get(server, params=params)
    def_spn = spn
    def_ll = ll
    return response


def write_image():
    global response, map_file
    with open(map_file, "wb") as file:
        file.write(response.content)


def draw_image():
    global screen, mp
    if mp:
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()


def draw_text_input():
    global input_box, color, text
    font = pygame.font.Font(None, 32)
    txt_surface = font.render(text, True, color)
    width = max(200, 300)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, color, input_box, 2)
    pygame.display.flip()


def draw():
    global screen, lst, n, address
    screen.fill((0, 0, 0))
    draw_image()
    draw_text_find(screen, 'Искать')
    draw_button_switch(screen, lst[n])
    draw_button_plus(screen, '+')
    draw_button_minus(screen, '-')
    draw_button_reset(screen, 'reset')
    address_text(screen, address)
    draw_box_index(screen)
    draw_text_for_index_box(screen, 'Индекс')
    draw_text_input()


def search_coord(text):
    global address, index, index_status
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
            address = resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['formatted']
            if 'postal_code' in resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']:
                index = resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['postal_code']
            if index_status:
                address += ' ' + index
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

input_box = pygame.Rect(300, 418 - 55, 240, 32)
input_box2 = ''
input_box3 = ''
box_plus = ''
box_minus = ''
box_reset = ''
box_index = ''

color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
t = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                t = True
                if box_index.collidepoint(event.pos):
                    index_status = not index_status
                    search_coord(address)
                elif box_plus.collidepoint(event.pos) and s > 0:
                    s -= 1
                    def_spn = str(sz_lst[s]) + ',' + str(sz_lst[s])
                    response = get_request(ll=def_ll, pt=def_pt, l=def_l, spn=def_spn)
                    write_image()
                elif box_minus.collidepoint(event.pos) and s < 3:
                    s += 1
                    def_spn = str(sz_lst[s]) + ',' + str(sz_lst[s])
                    response = get_request(ll=def_ll, pt=def_pt, l=def_l, spn=def_spn)
                    write_image()
                elif input_box2.collidepoint(event.pos):
                    ll = search_coord(text)
                    if ll != 0:
                        dr = True
                        mp = True
                        t = True
                        def_pt = ll
                        def_ll = ll
                        response = get_request(ll=def_ll, pt=def_pt, l=def_l, spn=def_spn)
                        write_image()
                    text = ''
                elif input_box3.collidepoint(event.pos):
                    n += 1
                    if n > 2:
                        n = 0
                    def_l = lst[n]
                    response = get_request(ll=def_ll, pt=def_pt, l=def_l, spn=def_spn)
                    write_image()
                elif box_reset.collidepoint(event.pos):
                    mp = False
                    address = ''
                    dr = False
                    write_image()
                elif not input_box.collidepoint(event.pos) and not box_minus.collidepoint(event.pos) and not box_plus.collidepoint(event.pos):
                    xr = size_lst[s][0] / 300
                    yr = size_lst[s][1] / 225
                    xx, yy = event.pos
                    xx, yy = xx * xr, yy * yr
                    def_ll = [float(i) for i in def_ll.split(',')]
                    def_pt = def_ll[0] - size_lst[s][0] + xx, def_ll[1] + size_lst[s][1] - yy
                    def_pt = ','.join(str(i) for i in def_pt)
                    def_ll = ','.join(str(i) for i in def_ll)
                    if dr:
                        search_coord(def_pt)
                        response = get_request(ll=def_ll, pt=def_pt, l=def_l, spn=def_spn)
                        write_image()
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                pos = [float(i) for i in def_ll.split(',')]
                if event.key == pygame.K_UP:
                    pos[1] += mashtab_lst[s]
                    def_ll = ','.join(str(i) for i in pos)
                    t = True
                    response = get_request(ll=def_ll, pt=def_pt, l=def_l, spn=def_spn)
                    write_image()
                if event.key == pygame.K_DOWN:
                    pos[1] -= mashtab_lst[s]
                    def_ll = ','.join(str(i) for i in pos)
                    t = True
                    response = get_request(ll=def_ll, pt=def_pt, l=def_l, spn=def_spn)
                    write_image()
                if event.key == pygame.K_LEFT:
                    pos[0] -= mashtab_lst[s]
                    def_ll = ','.join(str(i) for i in pos)
                    t = True
                    response = get_request(ll=def_ll, pt=def_pt, l=def_l, spn=def_spn)
                    write_image()
                if event.key == pygame.K_RIGHT:
                    pos[0] += mashtab_lst[s]
                    def_ll = ','.join(str(i) for i in pos)
                    t = True
                    response = get_request(ll=def_ll, pt=def_pt, l=def_l, spn=def_spn)
                    write_image()
            elif active:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    continue
                if event.key == pygame.K_RETURN:
                    t = True
                    dr = True
                    ll = search_coord(text)
                    if ll != 0:
                        mp = True
                        def_pt = ll
                        def_ll = ll
                        response = get_request(ll=def_ll, pt=def_pt, l=def_l, spn=def_spn)
                        write_image()
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    t = True
                    text = text[:-1]
                else:
                    t = True
                    text += event.unicode
    if t:
        draw()
        t = False


pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)