from pygame import *

display.set_caption('Ping Pong')
window = display.set_mode((700, 500))
background = transform.scale(image.load('ItsBack.png'), (700, 500))


class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       sprite.Sprite.__init__(self)


       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.withouttt = with_without


       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
   def __init__(key_upwards, key_downwards):
    self.key_down = key_downwards
    self.key_up = key_upwards
   def update(self):
       keys = key.get_pressed()
       if keys[self.key_up] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[self.key_down] and self.rect.y < 480:
           self.rect.y += self.speed



game = True

while game:
    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    time.delay(50)

