#ALL OF THE PICTURES FOR THE BACKGROUNDS I MADE MYSELF BY ELLA-ROSE LEVY
#SPRITES MADE BY ORC's 2D CHARCATER SPRITES 
import pygame, os, random, time
import datetime, operator

os.system('cls')
pygame.init()

#lists for menu messages

main_menu_list = ["Level 1", "Level 2", "Level 3" , "Leaderboard", "Settings", "Exit Game"]
settings_menu_list = ["Sprite selection", "Window size", "Background color", "Escape",]
leaderboard_menu_list = ["Escape"]

background_color_list=['white', 'green', 'black', 'back to settings',]
text_color_list=['gray', 'purple', 'black', 'back to settings',]
window_size_list=['small', 'medium', 'large', 'back to settings']
#storing positions for menu options, populated in show_menu_options function 
menu_options_positions = {}

#global colors defined as constants
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (150,0,0)
PURPLE = (150,0,150)
GREEN = (0,200,0)
GRAY = (169,169,169)

background_color = WHITE
font_color = GRAY

#window sizes 
window_sizes = {
    'small': {
        'width': 600,
        'height': 600
    },
    'medium': {
        'width': 800,
        'height': 600
    },
    'large': {
        'width': 1000,
        'height': 600
    }
}
#initial value for window settings
#can be changed in settings by user
current_window_size = 'medium'
window_width = window_sizes[current_window_size]['width']
window_height = window_sizes[current_window_size]['height']
window=pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Lava Game")
x_offset = 0

#Declare Fonts
TITLE_FONTS = {
    'small': pygame.font.SysFont('comicsans', 50),
    'medium': pygame.font.SysFont('comicsans', 89),
    'large': pygame.font.SysFont('comicsans', 89)
}
MENU_FONTS = {
    'small': pygame.font.SysFont('comicsans',25),
    'medium': pygame.font.SysFont('comicsans',35),
    'large': pygame.font.SysFont('comicsans',35)
}
INSTRUCTIONS_FONTS = {
    'small': pygame.font.SysFont('comicsans', 15),
    'medium': pygame.font.SysFont('comicsans', 25),
    'large': pygame.font.SysFont('comicsans', 25)
}

current_menu = 'main'
scores = []
#Takes score from file and storeing it in memory 
if not os.path.exists('finalproject.txt'):
    with open('finalproject.txt', 'w'): pass
file = open('finalproject.txt', 'r')
for line in file.readlines():
    text = line.strip('\n')
    name = text.split('-')[0]
    score = int(text.split('-')[1])
    scores.append((name, score))

def sort_scores():
    global scores
    
    # https://stackoverflow.com/questions/53570558/python-sorting-a-leaderboard-from-highest-to-lowest-scores-and-top-5-external-f
    return sorted(scores, key=lambda tup: tup[1])
#save all scores to text file
def save_scores():
    global scores

    file = open('finalproject.txt', 'a')
    file.truncate(0)
    for score_tuple in scores:
        file.write(score_tuple[0] + '-' + str(score_tuple[1]) + '\n')
    file.close()

def display_title(title):
    text = TITLE_FONTS[current_window_size].render(title, True, GRAY)
    current_window_width = window_sizes[current_window_size]['width']
    title_x = (current_window_width / 2) - (text.get_width() / 2)
    title_y = 0
    window.blit(text, (title_x, title_y))
#based on clicked position passed as arguments return to word clicked
def word_for_coordinate(x,y):
    for key in menu_options_positions:
        word = key
        coordinates = menu_options_positions[key]
        if x >=  coordinates["startX"] and x <= coordinates['endX'] and  y >=  coordinates['startY'] and y <=  coordinates['endY']:
            return word
#takes a list of menu option and displays them
def show_menu_options(menu_options, orientation):
    global menu_options_positions
    global MENU_FONTS, current_window_size
    global window
#remove old menu option postion from memory
    menu_options_positions.clear()
    if orientation == 'vertical':
        current_x = 70
    elif orientation == 'horizontal':
        current_x = 120
    current_y = 200
    #print out instructions if on main menu
    if 'Settings' in menu_options:
        first_line = INSTRUCTIONS_FONTS[current_window_size].render('Stay on the platforms and reach the end', True, GREEN)
        second_line = INSTRUCTIONS_FONTS[current_window_size].render("Don't fall or you will die", True, GREEN)
        window.blit(first_line, (50, 95))
        window.blit(second_line, (50, 135))
    for word in menu_options:
#clickable red square on menu hight and width 
        square_width = 30
        square_height = 30
        square = pygame.Rect(current_x, current_y, square_width, square_height)
        pygame.draw.rect(window, RED, square)
#storing where the boxes are 
        menu_options_positions[word] = {
            'startX': square.x,
            'endX': square.x + square_width,
            'startY': square.y,
            'endY': square.y + square_height
        }

        text = MENU_FONTS[current_window_size].render(word, True, GRAY)
        if orientation == 'vertical':
            text_x = current_x + square_width + 10
            if current_window_size == 'small':
                text_y = current_y - 5
            else:
                text_y = current_y - 15
        else:
            text_x = current_x + (square_width / 2) - (text.get_width() / 2)
            text_y = current_y + square_height + 10
            #display sprite on screen if the user is selecting their sprite 
            if 'Sprite' in word:
                sprite_index = int(word[len(word) - 1])
                window.blit(player_sprites[sprite_index]['left'][0], (text_x + 7, text_y + 30))
        window.blit(text, (text_x, text_y))
#adjust where to display the next menu function
        if orientation == 'vertical':
            current_y += 70
        elif orientation == 'horizontal':
            current_x += 150
#show the screen
def show_screen(screen_name, menu_options, orientation = 'vertical'):
    global cancel_seizure #cancle_seizure allowes the menu to refresh, 

    window.fill(background_color)
    display_title(screen_name)
    show_menu_options(menu_options, orientation)
    pygame.display.flip()
    cancel_seizure = True

# menu and level booleans 
show_main_menu = True
show_settings_menu = False
show_leaderboard_menu = False
show_result_screen = False
show_background_color_screen = False
show_sprite_selection_screen = False
show_window_size_screen = False
show_win_lose_screen = False
cancel_seizure = False
show_level = False
#game variables 
entered_name = ''
current_result = 'Lost'
current_level = 1

run=True

level_backgrounds = {
    1: pygame.image.load('finalproject/winter2.png'),
    2: pygame.image.load('finalproject/beach2.png'),
    3: pygame.image.load('finalproject/volcano.png'),
}
#key for the dictionary are the game levels
platform_positions = {
    1: [
        {
            'x': 0,
            'y': window_height - 10,
            'width': 150,
            'height': 10
        },
        {
            'x': 225,
            'y': window_height - 75,
            'width': 85,
            'height': 10
        },
        {
            'x': 350,
            'y': window_height - 150,
            'width': 85,
            'height': 10
        },
        {
            'x': 490,
            'y': window_height -250,
            'width': 85,
            'height': 10
        },
        {
            'x': 670,
            'y': window_height -370,
            'width': 85,
            'height': 10
        },
        {
            'x': 790,
            'y': window_height - 250,
            'width': 85,
            'height': 10
            
        },
        {
            'x': 950,
            'y': window_height - 150,
            'width': 85,
            'height': 10
        },
         {
            'x': 1080,
            'y': window_height - 250,
            'width': 85,
            'height': 10
            
        },
        
    ],
    2: [
        {'x': 0,
            'y': window_height - 10,
            'width': 150,
            'height': 10
        },
         {
            'x': 300,
            'y': window_height - 70,
            'width': 85,
            'height': 10
        },
        {
            'x': 495,
            'y': window_height - 260,
            'width': 85,
            'height': 10
        },
        {
            'x': 430,
            'y': window_height - 70,
            'width': 85,
            'height': 10
        },
        {
            'x': 550,
            'y': window_height - 70,
            'width': 85,
            'height': 10
        },
        {
            'x': 720,
            'y': window_height - 325,
            'width': 85,
            'height': 10
        },
        {
            'x': 900,
            'y': window_height - 450,
            'width': 85,
            'height': 10
        },
        {
            'x': 980,
            'y': window_height - 450,
            'width': 85,
            'height': 10
        },
        {
            'x': 325,
            'y': window_height - 200,
            'width': 85,
            'height': 10
        },
    ],
    3: [
        {
            'x': 0,
            'y': window_height - 20,
            'width': 85,
            'height': 20
        },
        
        {
            'x': 160,
            'y': window_height - 100,
            'width': 85,
            'height': 20
        },
        
        {
            'x': 410,
            'y': window_height - 100,
            'width': 85,
            'height': 20
        },
        {
            'x': 670,
            'y': window_height - 100,
            'width': 85,
            'height': 20
        },
        {
            'x': 920,
            'y': window_height - 100,
            'width': 85,
            'height': 20
        },

        {
            'x': 1110,
            'y': window_height - 100,
            'width': 85,
            'height': 20
        },
    ]
}
#platforms the player can stand on without dying
platforms = {}
def load_platforms():
    global platforms, platform_positions

    for level in range(1, 4):
        platforms[level] = []
        for platform_position in platform_positions[level]:
            platforms[level].append(pygame.Rect(platform_position['x'], platform_position['y'], platform_position['width'], platform_position['height']))
load_platforms()
#PLAYER VARIABLES including speed and jump
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 100
player_sprites = {}
current_selected_sprite = 1
was_walking_right = True
speed = 8
JUMP_CYCLES = 10
jump_count = 10
jump_speed = 30
jumping = False

#loading spites into memory
def load_player_sprites():
    global player_sprites

    for index in range(1, 4):
        player_sprites[index] = { 'left': [], 'right': [] }
        for image_index in range(10):
            player_sprites[index]['left'].append(
                pygame.transform.scale(pygame.image.load('finalproject/sprites/character' + str(index) + '/left' + str(image_index) + '.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
            )
            player_sprites[index]['right'].append(
                pygame.transform.scale(pygame.image.load('finalproject/sprites/character' + str(index) + '/right' + str(image_index) + '.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
            )
load_player_sprites()
#offset messure how far we have moved the background
def display_background(current_level):
    global level_background
#offset messure how far we have moved the background
    current_background = level_backgrounds.get(current_level)
    level_background.x = 0 + x_offset
    level_background = window.blit(current_background, level_background)

def display_character_sprite(add_x_offset = 0):
    global current_selected_sprite, walking_direction, player_walking_index
    global player

    current_player_image = player_sprites.get(current_selected_sprite).get(walking_direction)[player_walking_index]
    #only adjust offset when actually moving the background 
    player.x += add_x_offset
    player = window.blit(current_player_image, player)
#offset messure how far we have moved the background
def display_platforms(add_x_offset = 0):
    global platforms, current_level

    for platform in platforms[current_level]:
        platform.x += add_x_offset
        pygame.draw.rect(window,GREEN,platform)
#switching screens for a menu screen
def toggle_menu(menu_name):
    global show_main_menu
    global show_settings_menu
    global show_leaderboard_menu
    global show_result
    global cancel_seizure
    global show_background_color_screen
    global show_sprite_selection_screen
    global show_window_size_screen
    global show_win_lose_screen
    global current_menu
#resetting menu booleans 
    show_main_menu = False
    show_settings_menu = False
    show_leaderboard_menu = False
    show_result_screen = False
    cancel_seizure = False
    show_background_color_screen = False
    show_sprite_selection_screen = False
    show_window_size_screen = False
    show_win_lose_screen = False

#condition decide what menu to show 
    current_menu = menu_name
    if menu_name == 'main':
        show_main_menu = True
    elif menu_name == 'settings':
        show_settings_menu = True
    elif menu_name == 'leaderboard':
        show_leaderboard_menu = True
    elif menu_name == 'result':
        show_result_screen = True
    elif menu_name == 'background_color':
        show_background_color_screen = True
    elif menu_name == 'sprite_selection':
        show_sprite_selection_screen = True
    elif menu_name == 'window_size':
        show_window_size_screen = True
    elif menu_name == 'win_lose':
        show_win_lose_screen = True

#main loop for running game and menu
while run:
#redfresh the menu only if we want to
    if not cancel_seizure:
        if show_main_menu:
            show_screen('Main Menu', main_menu_list)
#append to settings current name
        elif show_settings_menu:
            calculated_menu = []
            for list_item in settings_menu_list:
                calculated_menu.append(list_item)
            calculated_menu.append('Current name: ' + entered_name)
            show_screen('Settings', calculated_menu)
#append the highest scores
        elif show_leaderboard_menu:
            calculated_menu = []
            sorted_scores = sort_scores()
            for index, sorted_score_tuple in enumerate(sorted_scores):
                if index <= 4:
                    calculated_menu.append(sorted_score_tuple[0] + ' - ' +  str(sorted_score_tuple[1]))
            for list_item in leaderboard_menu_list:
                calculated_menu.append(list_item)
            show_screen('Leaderboard', calculated_menu)

        elif show_background_color_screen:
            show_screen('Background color', ['White', 'Black'], 'horizontal')

        elif show_sprite_selection_screen:
            show_screen('Sprite selection', ['Sprite 1', 'Sprite 2', 'Sprite 3'], 'horizontal')

        elif show_window_size_screen:
            show_screen('Window sizes', ['Small', 'Medium', 'Large', 'Escape'])

        elif show_win_lose_screen:
            menu_options = []
            if current_result == 'Won':
                # https://stackoverflow.com/questions/3426870/calculating-time-difference 
                #calculate the time it took to win
                different_in_time = win_time - start_time
                seconds = round(different_in_time.total_seconds())
                menu_options.append('You won in ' + str(seconds) + ' seconds')
                scores.append((entered_name, seconds))
                save_scores()
            menu_options.append('Escape')
            show_screen('You ' + current_result, menu_options)

    if show_level:
        # current_level holds the current level the player is on
        # game logic here
        key_pressed = pygame.key.get_pressed()
        original_y = player.y
        player.y += 15 # apply gravity
        for platform in platforms[current_level]:
            if player.colliderect(platform):
                player.y = original_y
        #if player hits escape it brings them back to the main menu
        if key_pressed[pygame.K_ESCAPE]:
            cancel_seizure = False
            show_level = False
            toggle_menu('win_lose')
            x_offset = 0
#incremnet the player spite shown (player moving)
        if key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_RIGHT]:
            if player_walking_index >= 9:
                player_walking_index = -1
            player_walking_index += 1

        if key_pressed[pygame.K_LEFT]:
            if was_walking_right:
                player_walking_index = 0
                walking_direction = 'left'
                was_walking_right = False
            original_player_x = player.x
            player.x -= speed
            # # Before render, check if player has collided with the boulder
            for index in range(len(platforms[current_level])):
                if player.colliderect(platforms[current_level][index]):
                    player.x = original_player_x
                    

        if key_pressed[pygame.K_RIGHT]:
            if not was_walking_right:
                player_walking_index = 0
                walking_direction = 'right'
                was_walking_right = True
            original_player_x = player.x
            player.x += speed
            #cheeking the platforms for the current level
            for index in range(len(platforms[current_level])):
                if player.colliderect(platforms[current_level][index]):
                    player.x = original_player_x
                   

        if jumping:
            # if jump count is greater than or equal to -7
            if jump_count >= -JUMP_CYCLES:
                player.y -= jump_count * jump_speed / 5
                jump_count -= 1
            else:
                jump_count=JUMP_CYCLES
                jumping=False
                #if you collided while jumping
            for index in range(len(platforms[current_level])):
                if player.colliderect(platforms[current_level][index]):
                    if player.y + PLAYER_HEIGHT > platform_positions[current_level][index]['y'] + platform_positions[current_level][index]['height']:
                        player.y += (jump_count + 1) * jump_speed / 5
                    else:
                        player.y = platform_positions[current_level][index]['y'] - PLAYER_HEIGHT
                    jump_count = JUMP_CYCLES
                    jumping = False
        else:
            if key_pressed[pygame.K_SPACE]:
                jumping=True
#clearing positions for menu opiption when in game
        menu_options_positions.clear()
        #calculating additional x offset in this game loop
        x_offset_happened = 0
        current_window_width = window_sizes[current_window_size]['width']
        #adjusting offset based on player possition. Logic for scrolling screen
        if player.x + (PLAYER_WIDTH / 2) >= current_window_width * .8 and current_window_width - x_offset < level_backgrounds[current_level].get_width():
            x_offset -= speed
            x_offset_happened = -1 * speed
             #adjusting offset based on player possition.
        elif player.x <= current_window_width * .3 and x_offset <= 0:
            x_offset += speed
            x_offset_happened = speed
            if x_offset > 0:
                x_offset = 0
                x_offset_happened = 0
                #displaying things after the game loop
        display_background(current_level)
        display_character_sprite(x_offset_happened)
        display_platforms(x_offset_happened)
        #checking if the player fell in lava
        if player.y - 10 > window_height - PLAYER_HEIGHT:
            current_result = 'Lost'
            cancel_seizure = False
            show_level = False
            toggle_menu('win_lose')
            x_offset = 0
            #cheeking if the player has won
        if player.x + PLAYER_WIDTH - x_offset >= level_backgrounds[current_level].get_width() - 15:
            #if they are on a level below 3 continue on or go on to winning menu
            if current_level == 3:
            #resetting menu variables
                current_result = 'Won'
                cancel_seizure = False
                show_level = False
                toggle_menu('win_lose')
                x_offset = 0
                win_time = datetime.datetime.now()
            else:
            #resetting game variables 
                current_level += 1
                player_walking_index = 0
                walking_direction = 'right'
                current_player_image = player_sprites.get(current_selected_sprite).get(walking_direction)[player_walking_index]
                player = window.blit(current_player_image, (10, 10))
                current_background = level_backgrounds.get(current_level)
                level_background = window.blit(current_background, (0, 0))
                x_offset = 0
                
        pygame.display.update()
#if the player hits the X button escape
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        pygame.event.clear()
    
    else:
        # Menu logic
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
            #entering your name in the settings menu
                key_pressed = pygame.key.name(event.key)
                letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                if current_menu == 'settings':
                    if key_pressed in letters:
                        entered_name += key_pressed
                    if key_pressed == 'backspace':
                        entered_name = entered_name[:-1]
                    if key_pressed == 'space':
                        entered_name += ' '
                    toggle_menu('settings')
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pressed=pygame.mouse.get_pressed()
                if mouse_pressed[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    x_coordinate = mouse_pos[0]
                    y_coordinate = mouse_pos[1]

                    word_clicked = word_for_coordinate(x_coordinate, y_coordinate)

                    # Selecting a level

                    if word_clicked == 'Level 1' or word_clicked == 'Level 2' or word_clicked == 'Level 3':
                    #click 1 2 or 3 load the game for the level 
                        player_walking_index = 0
                        walking_direction = 'right'
                        current_player_image = player_sprites.get(current_selected_sprite).get(walking_direction)[player_walking_index]
                        player = window.blit(current_player_image, (10, 10))
                        current_background = level_backgrounds.get(current_level)
                        level_background = window.blit(current_background, (0, 0))
                        x_offset = 0
                        load_platforms()
                        start_time = datetime.datetime.now()


                    if word_clicked == 'Level 1':
                        show_level = True
                        current_level = 1
                    elif word_clicked == 'Level 2':
                        show_level = True
                        current_level = 2
                    elif word_clicked == 'Level 3':
                        show_level = True
                        current_level = 3
#toggle menu conditionals
                    elif word_clicked == 'Settings':
                        toggle_menu('settings')
                    elif word_clicked == 'Leaderboard':
                        toggle_menu('leaderboard')

                    elif word_clicked == 'Sprite selection':
                        toggle_menu('sprite_selection')
                    elif word_clicked == 'Sprite 1':
                        current_selected_sprite = 1
                        toggle_menu('settings')
                    elif word_clicked == 'Sprite 2':
                        current_selected_sprite = 2
                        toggle_menu('settings')
                    elif word_clicked == 'Sprite 3':
                        current_selected_sprite = 3
                        toggle_menu('settings')

                    elif word_clicked == 'Background color':
                        toggle_menu('background_color')
                    elif word_clicked == 'White':
                        background_color = WHITE
                        toggle_menu('settings')
                    elif word_clicked == 'Black':
                        background_color = BLACK
                        toggle_menu('settings')

                    elif word_clicked == 'Window size':
                        toggle_menu('window_size')
                    elif word_clicked == 'Small' and current_menu == 'window_size':
                        width = window_sizes.get('small').get('width')
                        height = window_sizes.get('small').get('height')
                        window = pygame.display.set_mode((width,height))
                        current_window_size = 'small'
                        toggle_menu('settings')
                    elif word_clicked == 'Medium' and current_menu == 'window_size':
                        width = window_sizes.get('medium').get('width')
                        height = window_sizes.get('medium').get('height')
                        window = pygame.display.set_mode((width,height))
                        current_window_size = 'medium'
                        toggle_menu('settings')
                    elif word_clicked == 'Large' and current_menu == 'window_size':
                        width = window_sizes.get('large').get('width')
                        height = window_sizes.get('large').get('height')
                        window = pygame.display.set_mode((width,height))
                        current_window_size = 'large'
                        toggle_menu('settings')
                    elif word_clicked == "Exit Game":
                        run = False
                        pygame.quit()
                        quit()
#Return to main menu function
                    elif word_clicked == 'Escape':
                        toggle_menu('main')

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
    #15 milliseconds between each game loop
    pygame.time.delay(15)

    


pygame.quit()
