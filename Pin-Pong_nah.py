#Создай собственный Шутер!
from time import time as timer
from pygame import *
from random import * 

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("The Ping-Pong")
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

        if key_pressed[K_s] and self.rect.y < 395:
            self.rect.y+= self.speed

    def update_Up_Down(self):     
            
        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y-= self.speed

        if key_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y+= self.speed
font.init()
text_of_pryamougolniki = font.Font(None, 80)
win_red = text_of_pryamougolniki.render('Red win', True, (0, 255, 0))
win_blue = text_of_pryamougolniki.render('blue win', True, (0, 255, 0))

ball = GameSprite("Ball.png", 320, 220, 10, 25, 25)
red = Player("Krasnuy_P.png", 0, 180, 10, 12, 100)
blue = Player("Siniy_P.png", 688, 180, 10, 12, 100)

ball_sx = 6
ball_sy = 6

black=(0,0,0)
finish = False
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(black)

        ball.rect.x += ball_sx
        ball.rect.y += ball_sy
        if ball.rect.y < 0 or ball.rect.y > 500 -30:
            ball_sy *= -1      


        if sprite.collide_rect(ball, red):
            ball_sx *= -1
        if sprite.collide_rect(ball, blue):
            ball_sx *= -1

        if ball.rect.x < 0:
            window.blit(win_blue, (230,210))
            finish = True

        if ball.rect.x > 700 -30:
            window.blit(win_red, (230,210))
            finish = True

        red.update_W_S()
        red.reset()

        blue.update_Up_Down()
        blue.reset()

        ball.reset()


    display.update()
    clock.tick(FPS)