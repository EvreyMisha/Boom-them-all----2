import pygame
import random

clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Крес")
pygame.font.init()
allBombs = pygame.sprite.Group()
bomb = pygame.image.load("data/bomb.png")
boom = pygame.image.load("data/boom.png")
x,y = 0,0
speed = 10
bombs = []
ch = []

sprits = [bomb, boom]


class Bomb(pygame.sprite.Sprite):

    def __init__(self, allBombs):
        pygame.sprite.Sprite.__init__(self)
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 500)
        self.rect = sprits[0].get_rect(centerx=self.x, bottom=self.y)


        while pygame.sprite.spritecollideany(self, allBombs):
            self.x = random.randint(0, 500)
            self.y = random.randint(0, 500)
            self.rect = sprits[0].get_rect(centerx=self.x, bottom=self.y)
        self.add(allBombs)
        self.stats = False

    def check(self):
        return pygame.sprite.collide_mask(self.rect)


    def click(self):
        if self.x<pygame.mouse.get_pos()[0]<self.x+50:
            if self.y < pygame.mouse.get_pos()[1] < self.y + 51:
                self.stats = True

    def draw(self):
        if self.stats:
            screen.blit(sprits[1],(self.x,self.y))
        else:
            screen.blit(sprits[0], (self.x, self.y))


running = True
for i in range(20):
    M = Bomb(allBombs)
    bombs.append(M)


while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in bombs:
                i.click()


    screen.fill((255,255,255))
    for i in bombs:
        i.draw()
    pygame.display.flip()


pygame.quit()