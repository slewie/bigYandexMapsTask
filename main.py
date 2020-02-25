import pygame
import requests
import os


def print_text(scree, text, x, y, font_size=50, color='white'):
    font_type = pygame.font.Font(None, font_size)
    mes = font_type.render(text, 1, pygame.Color(color))
    scree.blit(mes, (x, y))


class Button:
    def __init__(self, width, height, inactive_color=(150, 150, 150), active_color=(0, 0, 0), text_size=50,
                 font_type='cosm.ttf'):
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.text_size = text_size
        self.font_type = font_type
        self.action = None

    def draw(self, x, y, text, action=None, param_action=None, color='white'):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(screen, self.active_color, (x, y, self.width, self.height))
            if click[0] == 1:
                if action is not None:
                    if action == quit:
                        pygame.quit()
                        quit()
                    else:
                        if param_action:
                            action(param_action)
                            return
                        action()
                        return
        else:
            pygame.draw.rect(screen, self.inactive_color, (x, y, self.width, self.height))
        print_text(screen, text, x + 10, y + 15, font_size=self.text_size, color=color)


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


# блок работы с API карт
static_server = "https://static-maps.yandex.ru/1.x/?"
static_params = {"l": 'map',
                 "ll": "37.620070,55.753630"}
geocoder_server = "https://geocode-maps.yandex.ru/1.x/?"
geocoder_params = {"apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                   "geocode": None}

static_params["z"] = input("введите масштаб(0-17): ")
static_params["ll"] = input("долгота и широта ч/з запятую: ")

# блок pygame
pygame.init()
size = WIDTH, HEIGHT = 600, 450
screen = pygame.display.set_mode(size)
FPS = 10
clock = pygame.time.Clock()
running = True

main_map = get_mapimg(static_params)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(main_map, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)
try:
    os.remove('map.png')
except FileNotFoundError:
    pass
