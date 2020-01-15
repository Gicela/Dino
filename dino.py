import pygame

from pygame.locals import *

pygame.init()

screen_width=1000
screen_height=200
screen=pygame.display.set_mode([screen_width,screen_height])

#Dino variables

dinoSize = 100
dinox = 50
dinoy = 50
dinovx = 1.0
dinovy = 0.0
moveSpeed = 1.0
maxSpeed = 10.0
jumpHeight = 25.0
gravity = 1.0

#keyboard variables
rightDown = False
haveJumped = False

def move():
    global dinox, dinovx, dinovy, dinoy, moveSpeed, gravity, maxSpeed, jumpHeight, rightDown, haveJumped
    if rightDown:
        if dinovx < 0.0:
            dinovx = moveSpeed
            
    if dinox + dinoSize < screen_width:
        dinox += dinovx

    if dinovy > 1.0:
        dinovy = dinovy *0.9
    else:
        dinovy = 0.0
        haveJumped = False
    if dinoy < screen_height - dinoSize:
        dinoy += gravity
        gravity = gravity * 1.1
    else:
        dinoy = screen_height - dinoSize
        gravity = 1.0

    dinoy -= dinovy

    if (dinovx > 0.0 and dinovx < maxSpeed) or (dinovx < 0.0 and dinovx > -maxSpeed):
        if not haveJumped and (rightDown):
            dinovx = dinovx * 1.1
        
        
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
        dino = pygame.image.load("dino.png")

        dinorect = dino.get_rect()
      
        screen.blit(dino, (dinox, dinoy), dinorect)

        move()
        pygame.display.update()

