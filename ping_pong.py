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

ROCKET_ONE = Player('tennis_recket.png',50, 424,17,90,125)
ROCKET_TWO = Player('tennis_rocket.png',620, 424, 17,90,125)
BALLI =GameSprite('GRAN.png',200, 324, 2,70,70)
font.init()
font1 = font.Font(None,40)
lose1 = font1.render('ИГРОК 1 ПРОИГРАЛ!',True,(180,0,5))
lose2 = font1.render('ИГРОК 2 ПРОИГРАЛ!',True,(180,0,5))


clock = time.Clock()
FPS = 60
speed_x = 5
speed_y = 5
RUN_GAME = True
FINISH_GAME = False
while RUN_GAME:                     #!!!ГЕЙМПЛЕЙ!!!

    for e in event.get():
        if e.type == QUIT:      #выход из игры
            RUN_GAME = False

    window.blit(background,(0,0))
    if FINISH_GAME != True:
        BALLI.rect.x += speed_x
        BALLI.rect.y += speed_y

    if BALLI.rect.y > win_height-70 or BALLI.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(ROCKET_ONE, BALLI) or sprite.collide_rect(ROCKET_TWO,BALLI):
        speed_x *= -1

    if BALLI.rect.x < 0:
        FINISH_GAME = True
        window.blit(lose1,(200,200))

    if BALLI.rect.x > win_width:
        FINISH_GAME = True
        window.blit(lose2,(200,200))

    ROCKET_ONE.update_L()
    ROCKET_TWO.update_R()
    ROCKET_ONE.reset()
    
    ROCKET_TWO.reset()

    BALLI.reset()

    display.update()
    clock.tick(FPS)
    #!ВНИМАНИЕ!ФАЙЛ НЕ ДОРАБОТАН!!!
