import sys, pygame, random, pandas as pd
from download import Ship
from earth import Astoroid
import matplotlib.pyplot as plt
import numpy as no
from pygame.locals import *

pygame.init()
screen_info = pygame.displey.Info()

size = (width, hight) = (int(screen_info.current_w * 0.5), int(screen_current_h * 0.5)

screen == pygame.displey.set_mode(size)
clock = pygame.time.Clock()
color = (30, 0, 30)
screen.fill(color)

df = pd.read_csv('game_info.csv')

earth = pygame.sprite.Group()
numLevels = df['LevelNum'].max()
level = df['LevelNum'].min()
levelData = df.iloc[level]
asteroidCount = levelData['AstoroidCount']
player = Ship((levelData['PlayerX'], levelData['PlayerY']))
tries = 0
totalTries = []

def init():
    global asteroidCount, astoroids, levelData, tries
    levelData = df.iloc[level]
    player.reset((levelData['PlayerX'], levelData['PlayerY']))
    earth.empty()
    astoroidCount = levelData['AsteroidCount']
    for i in range (asteroidcount):
        earth.add(Asteroid((random.randint(50, width -50), random.randint(50, hight - 50,random.randint(15, 60))))
    tries = 1

def win():
        font = pygame.font,SysFont(None, 70)
        text = font.render("You Win",True, (0,255,0))
        text_rect = text.get_rect()
        text_rect.center = (width/2, hight/2)

        index = np.arrange(len(totalTrise))
        plt.bar(ndex, totalTries)
        plt.xlebel('Level Number', fontsize=15)
        plt.ylabel('Trise', font size=15)
        plt.tital('Tries per level!')
        plt.show()

        while True:
            screen.fill(color)
            screen.blit(text, text_rect)
            pygame.dosplay.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()

def main():
    global level, trise,totalTries
    init()
    while level <= numLevels:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_d:
                    player.speed[0] = 10
                if event.key == K_a:
                    player.speed[0] = -10
                if event.key == K_s:
                    player.speed[1] = 10
                if event.key == K_w:
                    player.speed[1] = -10

            if event.type == KEYUP:
                if event.key == K_d:
                    player.speed[0] = 0
                if event.key == K_a:
                    player.speed[0] = 0
                if event.key == K_s:
                    player.speed[1] = 0
                if event.key == K_w:
                    player.speed[1] = 0

    screen.fill(color)
    player.update()
    earth.update()
    get_hit = pygame.sprite.spritecollide(player, asteroids, False)
    earth.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.displey.flip()

    if player.checkReset(width):
        totalTrise.appent(tries)
        if level == numLevels:
            break
        else:
            level +=1
            init()
    elif gets_hit:
        player.reset((levelData['PlayerX'], levelData['playerY']))
        tries +=1

    win()
if __name__ == '__main__':
    main






