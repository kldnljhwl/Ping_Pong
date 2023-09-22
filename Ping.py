from pygame import *
font.init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_wide, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_wide, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.wide = player_wide
        self.height = player_height
    def reset(self):
        mainwin.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def racket_one(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < 500 - self.height:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
    def racket_two(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < 500 - self.height:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
racket1 = Player('STICK.png', 680, 150, 3, 20, 80)
racket2 = Player('STICK.png', 0, 150, 3, 20, 80)
ball = GameSprite('Nimetön.png', 330, 250, 3, 40, 40)
speed_x =3
speed_y = 3
font1 = font.SysFont('Verdana', 40)
lose1 = font1.render('PLAYER 1 LOST!', True, (255, 0, 0 ))
lose2 = font1.render('PLAYER 2 LOST!', True, (255, 0, 0 ))
mainwin = display.set_mode((700, 500))
background = transform.scale(image.load('sky.png'), (700, 500))
clock = time.Clock()
FPS = 60
game = True
finish = False
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        mainwin.blit(background, (0, 0))
        racket1.racket_one()
        racket2.racket_two()
        ball.rect.x += speed_x
        ball.rect.y += speed_y 
        if ball.rect.y > 500 - ball.height or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            mainwin.blit(lose1, (200, 210))
        if ball.rect.x > 660:
            finish = True
            mainwin.blit(lose2, (200, 210))
        ball.reset()
        racket1.reset()
        racket2.reset()
        clock.tick(FPS)
        display.update()
