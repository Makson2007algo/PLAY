from pygame import *
from random import randint
mixer.init()
font.init()
window = display.set_mode((500, 500))
display.set_caption('play')
background = transform.scale(image.load('fon.jpg'),(700, 500))

clock = time.Clock()
FPS = 60
#mixer.music.load('space.ogg')
#mixer.music.play()
#fire_sound = mixer.Sound('fire.ogg')
font = font.SysFont('Arial',50)
win = font.render('YOU WIN!', True,(255, 0, 0))
lose = font.render('YOU LOSE!', True,(255, 0, 0))

game = True
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, x_size, y_size):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (x_size, y_size))        
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.x_size = x_size
        self.y_size = y_size
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_RIGHT] and self.rect.x < 350:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
 
#    def fire(self):
#        bullet = Bullet('bullet.png',self.rect.centerx, self.rect.top, 8, 30, 30)
#        bullets.add(bullet)
#class Enemy(GameSprite):
#    def update(self):
#        self.rect.y += self.speed 
#        global lost
#        if self.rect.y >= 500:
#            self.rect.y = 0
#            self.rect.x = randint(20,600)
#            lost += 1
#class Bullet(GameSprite):
#    def update(self):
#        self.rect.y -= self.speed 
#        if self.rect.y <= 0:
#            self.kill()
#bullets = sprite.Group()
#monsters = sprite.Group()
#asteroids = sprite.Group()
#for i in range(5):
#    monster = Enemy('enemy.png', randint(20,600), 0, randint(1,2), 60, 60)               
#    monsters.add(monster)
#for c in range(2):
#    asteroid = Enemy('asteroid.png', randint(20,600), 0, randint(1,2), 50, 50)
#    asteroids.add(asteroid)
#
player1 = Player('платформа.png', 190, 420, 6, 140, 40)


ball = GameSprite('ball.png', 40, 110, 7, 40, 40)

speed_x = 3
speed_y = 3


#font.init()
#font = font.SysFont('Arial', 70)
#lose1 = font.render('Player one lose', True, (180, 0, 0))



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    
#        elif e.type == KEYDOWN:
#            if e.key == K_SPACE:
#                fire_sound.play()
#                player.fire()
#            if e.key == K_v and finish == True:
#                for m in monsters:
#                    m.kill()
#                for b in bullets:
#                    b.kill()
#                for a in asteroids:
#                    a.kill()
#                lost = 0
#                kill = 0
#                for i in range(5):
#                    monster = Enemy('enemy.png', randint(20,600), 0, randint(1,2), 60, 60)               
#                    monsters.add(monster)
#                finish = False
#                for c in range(2):
#                    asteroid = Enemy('asteroid.png', randint(20,600), 0, randint(1,2), 50, 50)
#                    asteroids.add(asteroid)








    if finish != True:      
        window.blit(background,(0, 0))
        player1.update_l()
        player1.reset()
        ball.reset() 
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y < 0:
        speed_y*= -1 
    if ball.rect.x < 0 or ball.rect.x > 460:   
        speed_x*= -1
    if sprite.collide_rect(player1, ball):
        speed_y*= -1
    
    # if ball.rect.x > 675 :
        #finish = True
        #window.blit(lose2, (200, 200))

    
    #if ball.rect.x < -25:
        #finish = True
        #window.blit(lose1, (200, 200))
    display.update()
    clock.tick(FPS)