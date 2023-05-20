from pygame import*
from random import randint
window = display.set_mode((750, 500))
display.set_caption('Пинг-Понг')
background = transform.scale(image.load('background.png'),(750, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, weight, height, player_speed, p_x, p_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(weight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <= 410:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= 410:
            self.rect.y += self.speed

class Player2(GameSprite):
    def updateFoRball(self):
        


PlayerOne = Player('player.png', 30, 90, 20, 1, 250)
PlayerTwo = Player('player.png', 30, 90, 20, 720, 250)
Ball = Player2('ballpng.png', 45, 45, 30, 375, 250)

game = True       
while game:
    clock = time.Clock()
    clock.tick(60)
    window.blit(background, (0, 0))
    PlayerOne.update()
    PlayerOne.reset()
    PlayerTwo.update2()
    PlayerTwo.reset()
    Ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False           
    display.update()
