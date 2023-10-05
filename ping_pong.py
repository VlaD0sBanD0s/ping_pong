from pygame import *
from random import *
from time import time as timer
win_width = 700
win_height = 500

window = display.set_mode((win_width,win_height))
display.set_caption('Пинг-понг')                   #!Что смотрим? Довольно многообещающее название игры)0)

background = transform.scale(image.load('ONE_FONE.jpg'), (win_width,win_height))  






class GameSprite(sprite.Sprite):        #Отец
    def __init__ (self, player_image, player_x, player_y, player_speed,size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x , self.rect.y))

class Player(GameSprite):       #TODO Сына
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:        
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <win_height - 80:
            self.rect.y += self.speed
        
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:        
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <win_height - 80:
            self.rect.y += self.speed

ROCKET_ONE = Player('tennis_rocket.png',50, 424,17,90,125)
ROCKET_TWO = Player('tennis_rocket.png',620, 424, 17,90,125)
BALLI =GameSprite('tennis_ball.png',200, 324, 4,90,90)


clock = time.Clock()
FPS = 60

RUN_GAME = True

while RUN_GAME:                     #!!!ГЕЙМПЛЕЙ!!!

    for e in event.get():
        if e.type == QUIT:      #выход из игры
            RUN_GAME = False

    window.blit(background,(0,0))


    ROCKET_ONE.update_L()
    ROCKET_TWO.update_R()
    ROCKET_ONE.reset()
    
    ROCKET_TWO.reset()

    BALLI.reset()

    display.update()
    clock.tick(FPS)
    #!ВНИМАНИЕ!ФАЙЛ НЕ ДОРАБОТАН!!!