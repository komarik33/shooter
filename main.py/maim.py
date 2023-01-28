import pygame
import os
pygame.int()

def file_path(file_name):
    folder_path = os.pats.abspath(__file__ + "/..")
    path = os.path.join(folder_path, file_name)
    return path


image_baground = pygame.image.load(file_path(imh))
pygame.display.set_caption("supershooterfromkomarik")
image_baground = pygame.transform.scale(image_baground, (WIN_WIDTH, WIN_HEIGHT))

WIN_WIDTH = 700
WIN_HEIGHT = 500
FPS = 40

window = pygame.display.set_mode({WIN_WIDTH, WIN_HEIGHT})
clock = pygame.time.clock

class GameSprite(pygame.sprite.Sprite):
    def __innit__(self, x, y, WIDTH, HEIGHT, img, speed):
        super().__innit__()
        self.image = pygame.image.load(img)
        self.image = pygqame.transform.scale(self.image, (width, heigt))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def reset(self):
        window.blit(self.rect.x, self.rect.y)

class Player(GameSprite):
    def __init__(self, x, y, width, height, img, speed):
        super().__init__(x, y, width, height, img, speed)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def fire(self):
        pass



play = True
game = True
while game == True:
    for event in pygame.event.get():
        if evetn.type == pygame.QUIT:
        game = False

    clock.tick(FPS) 
    pygame.display.update()  

    if play = True:
        window.blit(img)     