#!/usr/bin/env python

import pygame
from pygame.locals import *  # noqa
import sys
import random
import os

class FlappyBird:
    def __init__(self):
        self.screen = pygame.display.set_mode((400, 708))
        self.bird = pygame.Rect(65, 50, 50, 50)
        self.background = pygame.image.load("assets/background.png").convert()
        self.birdSprites = [pygame.image.load("assets/1.png").convert_alpha(),
                            pygame.image.load("assets/2.png").convert_alpha(),
                            pygame.image.load("assets/dead.png")]
        self.wallUp = pygame.image.load("assets/bottom.png").convert_alpha()
        self.wallDown = pygame.image.load("assets/top.png").convert_alpha()
        self.gap = 150#130 파이프갭
        self.wallx = 400
        self.birdY = 350
        self.jump = 0
        self.jumpSpeed = 2 #10
        self.gravity = 2 #5
        self.dead = False
        self.sprite = 0
        self.counter = 0
        self.offset = random.randint(-110, 110)
        self.level = 60
        #self.deadcount = 0;
        self.pause=False

    def updateWalls(self):
        self.wallx -= 2
        if self.wallx < -80:
            self.wallx = 400
            self.counter += 1
            self.offset = random.randint(-110, 110)

    def birdUpdate(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
            self.jump -= 1
        else:
            self.birdY += self.gravity
            self.gravity += 0.2
        self.bird[1] = self.birdY
        upRect = pygame.Rect(self.wallx,
                             360 + self.gap - self.offset + 10,
                             self.wallUp.get_width() - 10,
                             self.wallUp.get_height())
        downRect = pygame.Rect(self.wallx,
                               0 - self.gap - self.offset - 10,
                               self.wallDown.get_width() - 10,
                               self.wallDown.get_height())
        if upRect.colliderect(self.bird):
            self.dead = True
            #self.deadcount += 1
        if downRect.colliderect(self.bird):
            self.dead = True
            #self.deadcount += 1
        if not 0 < self.bird[1] < 720:
            self.bird[1] = 50
            self.birdY = 50
            self.dead = False
            self.counter = 0
            self.wallx = 400
            self.offset = random.randint(-110, 110)
            self.gravity = 5

    def run(self):
        clock = pygame.time.Clock()
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 50)
        while True:#True    self.deadcount != 3
            clock.tick(self.level)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not self.dead:
                    if(event.type == pygame.MOUSEBUTTONDOWN or event.key == pygame.K_UP):
                        self.jump = 17
                        self.gravity = 5
                        self.jumpSpeed = 10

                    if(event.type != pygame.MOUSEBUTTONDOWN and event.key == pygame.K_RIGHT):
                        self.level += 10

                    if(event.type != pygame.MOUSEBUTTONDOWN and event.key == pygame.K_LEFT):
                        if(self.level>=70):
                            self.level -= 10

            self.screen.fill((255, 255, 255))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.wallUp,
                             (self.wallx, 360 + self.gap - self.offset))
            self.screen.blit(self.wallDown,
                             (self.wallx, 0 - self.gap - self.offset))
            self.screen.blit(font.render(str(self.counter),
                                         -1,
                                         (255, 255, 255)),
                             (200, 50))
            self.screen.blit(font.render(str(self.level), -1, (255, 255, 255)), (200, 658))
            if self.dead:
                self.sprite = 0#2
                self.level = 60
            elif self.jump:
                self.sprite = 2#1
            self.screen.blit(self.birdSprites[self.sprite], (70, self.birdY))
            if not self.dead:
                self.sprite = 2#0
            #일시정지 구현할 부분
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_p)and(self.pause==False):
                    self.pause = True
                    os.system("Pause")
                elif (event.key == pygame.K_p)and(self.pause==True):
                    self.pause=False
                    os.system("Pause")
            self.updateWalls()
            self.birdUpdate()
            pygame.display.update()

if __name__ == "__main__":
    
    FlappyBird().run()
