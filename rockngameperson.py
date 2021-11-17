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
WHITE = (255,255,255)
BLACK = (0,0,0)
TITLE_FONT=pygame.font.SysFont('comicsans', 80)
background = pygame.image.load("bgSmaller.jpg")

window.blit(background, (0,0))
#screen.blit(FIG, (300,300))
pygame.display.flip()
pygame.time.delay(1000)

pygame.display.set_caption('Boulder game')
pygame.display.flip()
pygame.time.delay(100)

is_game_running=True
has_won = False

GROUND_HEIGHT = 40

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
player_x = 10
player_y = WINDOW_HEIGHT - PLAYER_HEIGHT - GROUND_HEIGHT
player_image_index = -1
is_walking_left = True
is_walking_right = False
player = window.blit(player_walking_left[player_image_index], (player_x, player_y))
was_going_left = True

# BOULDER_WIDTH = 100
# BOULDER_HEIGHT = 200

# boulder_x = WINDOW_WIDTH-300
# boulder_y = WINDOW_HEIGHT-200
# boulder = pygame.Rect(boulder_x, boulder_y, BOULDER_WIDTH, BOULDER_HEIGHT)

rock_positions = [
    {
        'x': 183,
        'y': 365,
        'width': 50,
        'height': 75
    },
    {
        'x': WINDOW_WIDTH - 385,
        'y': WINDOW_HEIGHT - 205,
        'width': 145,
        'height': 200
    },
    {
        'x': WINDOW_WIDTH - 240,
        'y': WINDOW_HEIGHT - 275,
        'width': 15,
        'height': 10
    },
    {
        'x': WINDOW_WIDTH - 325,
        'y': WINDOW_HEIGHT - 325,
        'width': 10,
        'height': 10
    }
]
rocks = []
for rock_position in rock_positions:
    rocks.append(pygame.Rect(rock_position['x'], rock_position['y'], rock_position['width'], rock_position['height']))

HEIGHT_BACKGROUND_JUMPPOINT = 300
WIDTH_BACKGROUND_JUMPPOINT = 330
BACKGROUND_JUMPPOINT1 = 330

HEIGHT_FlOATING_BACKGROUND_JUMPPOINT = 600
WIDTH_FLOATING_BACKGROUND_JUMPPOINT = 660
FLOATING_JUMPPOINT = 234

HEIGHT_PEAK_BACKGROUND_JUMPPOINT = 700
WIDTH_PEAK_BACKGROUND_JUMPPOINT =730
PEAK_JUMPPOINT = 349

HEIGHT_MOON = 800
WIDTH_MOON = 890
MOON = 570
#elif x is < 80 jumping


JUMP_CYCLES = 10
jump_count = 10
jump_speed = 20
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

    original_y = player.y
    player.y += 15
    for rock in rocks:
        if player.colliderect(rock):
            player.y = original_y
    

    if key_pressed[pygame.K_LEFT]:
        was_going_left = True
        new_player_image = get_player_image('left')
        # Add/remove X or Y to move the player
        player.x -= speed
        # Before render, check if player has collided with the boulder
        for index in range(len(rocks)):
            if player.colliderect(rocks[index]):
                player.x = rock_positions[index]['x'] + rock_positions[index]['width']

    if key_pressed[pygame.K_RIGHT]:
        was_going_left = False
        new_player_image = get_player_image('right')
        player.x += speed
        for index in range(len(rocks)):
            if player.colliderect(rocks[index]):
                player.x = rock_positions[index]['x'] - PLAYER_WIDTH

    if key_pressed[pygame.K_DOWN]:
        player.y += speed
        for index in range(len(rocks)):
            if player.colliderect(rocks[index]):
                player.y = rock_positions[index]['y'] - PLAYER_HEIGHT

    
    if jumping:
        # if jump count is greater than or equal to -7
        if jump_count >= -JUMP_CYCLES:
            player.y -= jump_count * jump_speed / 5
            jump_count -= 1
        else:
            jump_count=JUMP_CYCLES
            jumping=False
        for index in range(len(rocks)):
            if player.colliderect(rocks[index]):
                if player.y + PLAYER_HEIGHT > rock_positions[index]['y'] + rock_positions[index]['height']:
                    player.y += (jump_count + 1) * jump_speed / 5
                else:
                    player.y = rock_positions[index]['y'] - PLAYER_HEIGHT
                jump_count = JUMP_CYCLES
                jumping = False
    else:
        if key_pressed[pygame.K_SPACE]:
            jumping=True


    if player.x < 0:
        player.x = 0
    if player.x > WINDOW_WIDTH-PLAYER_WIDTH:
        player.x = WINDOW_WIDTH - PLAYER_HEIGHT
    if player.y < 20:
        is_game_running = False
        has_won = True
    if player.y > WINDOW_HEIGHT - PLAYER_HEIGHT - GROUND_HEIGHT:
        player.y = WINDOW_HEIGHT - PLAYER_HEIGHT - GROUND_HEIGHT

    for rock in rocks:
        pygame.draw.rect(window,blue,rock)
    window.blit(background, (0,0))
   # screen.fill(green)
    window.blit(new_player_image, player)
    # pygame.draw.rect(window,(red),player)
    pygame.display.update()
    pygame.time.delay(20)


window.fill(WHITE)
text= TITLE_FONT.render('You WIN!',1,BLACK)
xm=WINDOW_WIDTH/2 - text.get_width()/2
ym=40
window.blit(text, (xm,ym))
pygame.display.update()
show_menu = False
pygame.time.delay(2000)
        
pygame.quit()
