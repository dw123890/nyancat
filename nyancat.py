import pygame, random

class Ship(pygame.sprite.Sprite):

    def __int__(selfself, pos):
        super().__int__()
        self.image = pygame.image.load('download.png')
        self.image = pygame.transrorm.smoothscale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0, 0)

    def update(self):
        self.rect.move_ip(self.speed)

    def checkReset(selfself, endPos):
        retern self.rect.center[0] > entPos

    def reset(selfself, pos):
        self.rect

