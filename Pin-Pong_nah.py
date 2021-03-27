#Создай собственный Шутер!
from time import time as timer
from pygame import *
from random import * 

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("ТОПА")
#Задай FPS 60 кадров/сек
FPS = 60
#Установи фоновую музыку
#mixer.init()
#mixer.music.load("turu-tu-tu.mp3")
#mixer.music.play()
#обработай событие «клик по кнопке "Закрыть окно"»
game = True
clock = time.Clock()
#Создай и отобрази спрайты для игрока и врага
lost = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_W_S(self):     
            
        key_pressed = key.get_pressed()

        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y-= self.speed

        if key_pressed[K_s] and self.rect.y < 430:
            self.rect.y+= self.speed

    def update_Up_Down(self):     
            
        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y-= self.speed

        if key_pressed[K_DOWN] and self.rect.y < 430:
            self.rect.y+= self.speed

red = Player("Krasnuy_P.png", 0, 10, 10, 10, 90)
blue = Player("Siniy_P.png", 690, 10, 10, 10, 90)

black=(0,0,0)
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill(black)
    red.update_W_S()
    red.reset()

    blue.update_Up_Down()
    blue.reset()

    display.update()
    clock.tick(FPS)