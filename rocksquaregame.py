# #ella-rose
# #10-20-21`
# #mouse position
# #drawing reject
# #moving object
# #K_UP                  up arrow
# #K_DOWN                down arrow
# #K_RIGHT               right arrow
# #K_LEFT                left arrow
# #K_INSERT              insert
# import os
# import pygame as py
# import random
import pygame, time, sys

pygame.init()
pygame.time.delay(100)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
white = [255,2555,255]
red = [255,0,0]
green = [0,200,0]
blue = [0,0,255]
background = pygame.image.load("bgSmaller.jpg")

window.blit(background, (0,0))
#screen.blit(FIG, (300,300))
pygame.display.flip()
pygame.time.delay(1000)

pygame.display.set_caption('Boulder game')
pygame.display.flip()
pygame.time.delay(100)

is_game_running=True

PLAYER_HEIGHT = 20
PLAYER_WIDTH = 20
player_x=20
player_y=20
square = pygame.Rect(player_x, player_y, PLAYER_HEIGHT, PLAYER_WIDTH)
rad= 30

BOULDER_WIDTH = 100
BOULDER_HEIGHT = 200
boulder_x = WINDOW_WIDTH-300
boulder_y = WINDOW_HEIGHT-200
boulder = pygame.Rect(boulder_x, boulder_y, BOULDER_WIDTH, BOULDER_HEIGHT)

JUMP_CYCLES = 7
jump_count = 7
jumping = False
speed = 10

while is_game_running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            is_game_running = False
    pygame.time.delay(5)
    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_LEFT]:
        # Add/remove X or Y to move the player
        square.x -= speed
        # Before render, check if player has collided with the boulder
        if square.colliderect(boulder):
            # Move the player back to edge of boulder (before refreshing screen)
            square.x = boulder_x + BOULDER_WIDTH

    if key_pressed[pygame.K_RIGHT]:
        square.x += speed
        if square.colliderect(boulder):
            square.x = boulder_x - PLAYER_WIDTH

    if key_pressed[pygame.K_DOWN]:
        square.y += speed
        if square.colliderect(boulder):
            square.y = boulder_y - PLAYER_HEIGHT
    
    if jumping:
        # if jump count is greater than or equal to -7
        if jump_count >= -JUMP_CYCLES:
            square.y -= jump_count * speed / 5
            jump_count -= 1
        else:
            jump_count=JUMP_CYCLES
            jumping=False
        if square.colliderect(boulder):
            square.y = boulder_y - PLAYER_HEIGHT
            jump_count=JUMP_CYCLES
            jumping=False
    else:
        if key_pressed[pygame.K_UP]:
            square.y -= speed
        if key_pressed[pygame.K_SPACE]:
            jumping=True

    if square.x < 0:
        square.x = 0
    if square.x > WINDOW_WIDTH-PLAYER_WIDTH:
        square.x = WINDOW_WIDTH - PLAYER_HEIGHT
    if square.y < 0:
        square.y = 0
    if square.y > WINDOW_HEIGHT - PLAYER_HEIGHT:
        square.y = WINDOW_HEIGHT - PLAYER_HEIGHT

    window.blit(background, (0,0))
   # screen.fill(green)
    pygame.draw.rect(window,(red),square)
    pygame.draw.rect(window,blue,boulder)
    pygame.display.update()
    pygame.time.delay(20)
        
pygame.quit()
