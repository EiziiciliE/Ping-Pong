#Создай собственный Шутер!
from time import time as timer
from pygame import *
from random import * 

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("ТОПА")
background = transform.scale(image.load("galaxy.jpg"),(700, 500))
#Задай FPS 60 кадров/сек
FPS = 60
#Установи фоновую музыку
mixer.init()
mixer.music.load("turu-tu-tu.mp3")
mixer.music.play()
fire_sosi = mixer.Sound("fire.ogg")
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
    def update(self):     
            
        key_pressed = key.get_pressed()

        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.x-= self.speed

        if key_pressed[K_s] and self.rect.x < 440:
            self.rect.x+= self.speed


while game:
    
    display.update()
    clock.tick(FPS)
