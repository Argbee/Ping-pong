from pygame import *

display.set_caption('Ping Pong')
window = display.set_mode((700, 500))
background = transform.scale(image.load('ItsBack.png'), (700, 500))


class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       sprite.Sprite.__init__(self)



       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed



       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))




class Player(GameSprite):
   def __init__(self, key_upwards, key_downwards, player_image, player_x, player_y, size_x, size_y, player_speed):
    GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y, player_speed)
    self.key_down = key_downwards
    self.key_up = key_upwards
   def update(self):
       
       keys = key.get_pressed()
       if keys[self.key_up] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[self.key_down] and self.rect.y < 480:
           self.rect.y += self.speed
       window.blit(self.image, (self.rect.x, self.rect.y))

font.init()
font1 = font.Font(None, 45)

lost1 = font1.render('Player 1 lost!', True, (180, 0, 0))
lost2 = font1.render('Player 2 lost!', True, (180, 0, 0))

balll = GameSprite('whiteBall.png', 310, 230, 50, 50, 5)
stick_1 = Player(K_w, K_s, 'stick_left.png', 10, 210, 20, 120, 5)
stick_2 = Player(K_UP, K_DOWN, 'stick_right.png', 670, 210, 20, 120, 5)
speed_x = 5
speed_y = 5

finish = False
game = True

while game:

    window.blit(background,(0,0))
    balll.reset()
    stick_1.update()
    stick_2.update()
    if finish != True:
        balll.rect.x += speed_x
        balll.rect.y += speed_y
        if balll.rect.y > 450 or balll.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(stick_1, balll) or sprite.collide_rect(stick_2, balll):
            speed_x *= -1
        if balll.rect.x < 0:
            finish = True
            playiir = 1

        if balll.rect.x > 699:
            finish = True
            playiir = 2
    if finish == True:
        if playiir == 1:
            window.blit(lost1, (240, 230))

        if playiir == 2:
            window.blit(lost2, (240, 230))


    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    time.delay(50)
