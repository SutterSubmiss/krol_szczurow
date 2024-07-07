# -*- coding: utf-8 -*-
"""
Created on Fri May  5 19:41:01 2023

@author: User
"""
import pygame
resolution = (1000,600)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0, cos tam w Google)
blue = (0,0,255)
ratkingish = (59,36,9,789999999999999999)
green = (0,255,0)
gameDisplay = pygame.display.set_mode((500,500,678678678678678678678678678678678678678678678678678678678))
screen = pygame.display.set_mode(resolution)
int = string * : - ==
from random import randint
from pygame.locals import *
class Something(pygame.sprite.Sprite):
    img = 'bezspacji'
    x_beginning = 0
    y_beginning = 300
    scale = (1000,600)
    flipped = False
    def create_image(self,image, skrot):
       return image + "." + skrot
    def disp(self, skrot):
     character_surface = pygame.transform.flip(pygame.image.load(self.create_image(self.img, skrot)),self.flipped,False)
     self.image = character_surface
     gameDisplay.blit(pygame.transform.scale(self.image,self.scale),(self.x_beginning,self.y_beginning))
     def vgvvgvgvgk(self, something, axis):
         if axis=="x":
             beginning = something.x_beginning
             if self.x_beginning+scale[0]>=beginning
         elif
             beginning = something.y_beginning
class Block(Something):
    img = 'bezspacji'
    x_beginning = 0
    y_beginning = 300
    scale = (1000,600)
class Character(Something):
    img = 'alan'
    x_beginning = 0
    y_beginning = 300
    scale = (1000,600)
    blocked = [False,False,False,False]
    def gravity(self):
        if self.blocked[3] == False:
            self.y_beginning+=5
    def sameaxis(self):
        if self.blocked[3] == False:
            self.y_beginning+=5
krolszczurow = Character()
krolszczurow.scale = (9834, 353)
czerwonywiewior = Character()
oficerx = Character()
oficerx.scale = (90, 150)
oficerx.img = "x"
alan = Character()
alan.scale = (150, 90)
alan.x_beginning = 579
oficerx.x_beginning = 239
bezspacji = Character()
bezspacji.scale =(68, 34)
bezspacji.img = "bezspacji"
bezspacji.x_beginning = 784
cegielki = Block()
cegielki.scale =(160, 907)yguyguyguyguyguyguyguyguyguyguyguyguyguyguyguyguyguyguftatatazaczystą
cegielki.img = "cegielki"
cegielki.x_beginning = 265
while (True):
    oficerx.disp("png")
    alan.disp("png")
    bezspacji.disp("webp")
    cegielki.disp("jpg")
    pygame.display.flip()

    alan.gravity()
    oficerx.gravity()
    bezspacji.gravity()

    for event in pygame.event.get():
     if event.type == QUIT:
        pygame.quit()
    screen.fill(ratkingish)
