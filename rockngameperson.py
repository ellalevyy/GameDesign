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

player_x=20
player_y=20
player_walking_left = [
    pygame.image.load('pictures/L1.png'),
    pygame.image.load('pictures/L2.png'),
    pygame.image.load('pictures/L3.png'),
    pygame.image.load('pictures/L4.png'),
    pygame.image.load('pictures/L5.png'),
    pygame.image.load('pictures/L6.png'),
    pygame.image.load('pictures/L7.png'),
    pygame.image.load('pictures/L8.png'),
    pygame.image.load('pictures/L9.png'),
]
player_walking_right = [
    pygame.image.load('pictures/R1.png'),
    pygame.image.load('pictures/R2.png'),
    pygame.image.load('pictures/R3.png'),
    pygame.image.load('pictures/R4.png'),
    pygame.image.load('pictures/R5.png'),
    pygame.image.load('pictures/R6.png'),
    pygame.image.load('pictures/R7.png'),
    pygame.image.load('pictures/R8.png'),
    pygame.image.load('pictures/R9.png'),
]
PLAYER_HEIGHT = pygame.Surface.get_height(player_walking_left[0])
PLAYER_WIDTH = pygame.Surface.get_width(player_walking_left[0])
player_image_index = -1
is_walking_left = True
is_walking_right = False
player = window.blit(player_walking_left[player_image_index], (player_x, player_y))
was_going_left = True

BOULDER_WIDTH = 100
BOULDER_HEIGHT = 200
boulder_x = WINDOW_WIDTH-300
boulder_y = WINDOW_HEIGHT-200
boulder = pygame.Rect(boulder_x, boulder_y, BOULDER_WIDTH, BOULDER_HEIGHT)

JUMP_CYCLES = 7
jump_count = 7
jumping = False
speed = 10

def get_player_image(direction):
    global player_image_index
    if player_image_index >= 8:
        player_image_index = -1
    player_image_index += 1
    if direction == 'left':
        return player_walking_left[player_image_index]
    else:
        return player_walking_right[player_image_index]


while is_game_running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            is_game_running = False
    pygame.time.delay(5)
    key_pressed = pygame.key.get_pressed()
    if was_going_left:
        new_player_image = player_walking_left[player_image_index]
    else:
        new_player_image = player_walking_right[player_image_index]

    if key_pressed[pygame.K_LEFT]:
        was_going_left = True
        new_player_image = get_player_image('left')
        # Add/remove X or Y to move the player
        player.x -= speed
        # Before render, check if player has collided with the boulder
        if player.colliderect(boulder):
            # Move the player back to edge of boulder (before refreshing screen)
            player.x = boulder_x + BOULDER_WIDTH

    if key_pressed[pygame.K_RIGHT]:
        was_going_left = False
        new_player_image = get_player_image('right')
        player.x += speed
        if player.colliderect(boulder):
            player.x = boulder_x - PLAYER_WIDTH

    if key_pressed[pygame.K_DOWN]:
        player.y += speed
        if player.colliderect(boulder):
            player.y = boulder_y - PLAYER_HEIGHT
    
    if jumping:
        # if jump count is greater than or equal to -7
        if jump_count >= -JUMP_CYCLES:
            player.y -= jump_count * speed / 5
            jump_count -= 1
        else:
            jump_count=JUMP_CYCLES
            jumping=False
        if player.colliderect(boulder):
            player.y = boulder_y - PLAYER_HEIGHT
            jump_count=JUMP_CYCLES
            jumping=False
    else:
        if key_pressed[pygame.K_UP]:
            player.y -= speed
        if key_pressed[pygame.K_SPACE]:
            jumping=True

    if player.x < 0:
        player.x = 0
    if player.x > WINDOW_WIDTH-PLAYER_WIDTH:
        player.x = WINDOW_WIDTH - PLAYER_HEIGHT
    if player.y < 0:
        player.y = 0
    if player.y > WINDOW_HEIGHT - PLAYER_HEIGHT:
        player.y = WINDOW_HEIGHT - PLAYER_HEIGHT

    window.blit(background, (0,0))
   # screen.fill(green)
    window.blit(new_player_image, player)
    # pygame.draw.rect(window,(red),player)
    pygame.draw.rect(window,blue,boulder)
    pygame.display.update()
    pygame.time.delay(20)
        
pygame.quit()
