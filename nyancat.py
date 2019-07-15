import pygame, random

class Ship(pygame.sprite.Sprite):

    def __int__(selfself, pos):
        super().__int__()
        self.image = pygame.image.load('ship.png')
