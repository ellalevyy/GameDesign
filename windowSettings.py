import pygame, os, random, time

os.system('cls')
pygame.init()

#lists for menu messages

main_menu_list=["Instructions","Settings","scoreboard", "Level 1", "Level 2", "Level 3" ,"escape"]
instructions_list = ['escape']
level1_list =['escape']
level2_list =['escape']
level3_list =['escape']
settings_list=["background color","window size", "text color", "escape",]
background_color_list=['white', 'green', 'black', 'back to settings',]
text_color_list=['gray', 'purple', 'black', 'back to settings',]
window_size_list=['small', 'medium', 'large', 'back to settings']
scoreboard_list=["escape"]
menu_options_positions = {}
#GLOBAL DICTIONARY

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (150,0,0)
PURPLE = (150,0,150)
GREEN = (0,200,0)
GRAY = (169,169,169)

background_color = WHITE
font_color = GRAY


window_sizes = {
    'small': {
        'width': 600,
        'height': 600
    },
    'medium': {
        'width': 800,
        'height': 800
    },
    'large': {
        'width': 1000,
        'height': 1000
    }
}

current_window_size = 'medium'
initial_window_width = window_sizes.get(current_window_size).get('width')
initial_window_height = window_sizes.get(current_window_size).get('height')
win=pygame.display.set_mode((initial_window_width, initial_window_height))
pygame.display.set_caption("Setting Window")

wbox=30
hbox=30
x=70
y=150

square=pygame.Rect(x,y, wbox, hbox)
#Declare Fonts
TITLE_FONTS = {
    'small': pygame.font.SysFont('comicsans', 50),
    'medium': pygame.font.SysFont('comicsans', 89),
    'large': pygame.font.SysFont('comicsans', 105)
}
MENU_FONTS = {
    'small': pygame.font.SysFont('comicsans',35),
    'medium': pygame.font.SysFont('comicsans',49),
    'large': pygame.font.SysFont('comicsans',65)
}
INSTRUCTIONS_FONTS = {
    'small': pygame.font.SysFont('comicsans', 15),
    'medium': pygame.font.SysFont('comicsans', 25),
    'large': pygame.font.SysFont('comicsans', 32)
}
text = TITLE_FONTS.get(current_window_size).render('message',1,font_color)
current_menu = 'Main Menu'

def display_TITLE(message):
    win.fill(background_color)
    # pygame.time.delay(100)
    title_font = TITLE_FONTS.get(current_window_size)
    text = title_font.render(message,1,font_color)
    current_window_width = window_sizes.get(current_window_size).get('width')
    xm = (current_window_width / 2) - (text.get_width() / 2)
    ym = 40
    win.blit(text, (xm,ym))
    pygame.display.update()
    # pygame.time.delay(100)

def Menu_function(messages):
    # pygame.time.delay(100)
    ym=y
    xm=x+wbox+10
    menu_options_positions.clear()
    for i in range(0,len(messages)):
        word=messages[i]
        square.y=ym
        menu_options_positions[word] = {
            'startX': square.x,
            'endX': square.x + wbox,
            'startY': square.y,
            'endY': square.y + hbox
        }
        pygame.draw.rect(win,RED, square)
        menu_font = MENU_FONTS.get(current_window_size)
        text = menu_font.render(word,1,font_color)
        win.blit(text,(xm,ym))
        pygame.display.flip()
        # pygame.time.delay(100)
        if(current_window_size == 'small'):
            y_offset = 50
        elif(current_window_size == 'medium'):
            y_offset = 80
        elif(current_window_size == 'large'):
            y_offset = 120
        ym += y_offset

def word_for_coordinate(x,y):
    for key in menu_options_positions:
        word = key
        coordinates = menu_options_positions[key]
        if x >=  coordinates["startX"] and x <= coordinates['endX'] and  y >=  coordinates['startY'] and y <=  coordinates['endY']:
            return word

def show_screen(screen_name, menu_list):
    win.fill(background_color)
    pygame.display.update()
    pygame.time.delay(100)
    display_TITLE(screen_name)
    Menu_function(menu_list)

# start of main code
show_main_menu = True

run=True

while run:
    if  show_main_menu == True:
        current_menu = 'Main Menu'
        win.fill(background_color)
        pygame.display.update()
        display_TITLE("Main Menu")
        Menu_function(main_menu_list)
        show_main_menu = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pressed=pygame.mouse.get_pressed()
            if mouse_pressed[0]:
                mouse_pos=pygame.mouse.get_pos()
                x_coordinate = mouse_pos[0]
                y_coordinate = mouse_pos[1]

                word_clicked = word_for_coordinate(x_coordinate, y_coordinate)

                if word_clicked == 'Instructions':
                    current_menu = word_clicked
                    myFile=open('instructions.txt', 'r')
                    display_TITLE('Instructions')
                    Menu_function(instructions_list)
                    pygame.time.delay(100)
                    current_y = 300
                    for line in myFile.readlines():
                        instructions_font = INSTRUCTIONS_FONTS.get(current_window_size)
                        text = instructions_font.render(line.strip('\n'), 1, font_color)
                        win.blit(text, (70, current_y))
                        current_y += 50
                        print(line)
                    pygame.display.update()
                    myFile.close()
                
                if word_clicked == 'Settings' or word_clicked == "back to settings":
                    current_menu = word_clicked
                    show_screen('Settings', settings_list)

                if word_clicked == 'Level 1':
                    current_menu = word_clicked
                    show_screen('Level 1', level1_list)
                    
                if word_clicked == 'Level 2':
                    current_menu = word_clicked
                    show_screen('Level 2', level2_list)

                if word_clicked == 'Level 3':
                    current_menu = word_clicked
                    show_screen('Level 3', level3_list)

                if word_clicked  =='scoreboard':
                    current_menu = word_clicked
                    show_screen('scoreboard', scoreboard_list)

                if word_clicked == 'background color':
                    current_menu = word_clicked
                    show_screen('background color', background_color_list)

                if word_clicked == 'text color':
                    current_menu = word_clicked
                    show_screen('text color', text_color_list)

                if word_clicked == 'window size':
                    current_menu = word_clicked
                    show_screen('window size', window_size_list)

                if word_clicked == 'escape':
                    pygame.display.update()
                    pygame.time.delay(100)
                    show_main_menu = True
                
                ### settings menu options

                if word_clicked == 'black' and current_menu == 'background color':
                    background_color = BLACK
                    show_screen('background color', background_color_list)

                if word_clicked == 'white' and current_menu == 'background color':
                    background_color = WHITE
                    show_screen('background color', background_color_list)

                if word_clicked == 'green' and current_menu == 'background color':
                    background_color = GREEN
                    show_screen('background color', background_color_list)

                if word_clicked == 'gray' and current_menu == 'text color':
                    font_color = GRAY
                    show_screen('text color', text_color_list)

                if word_clicked == 'purple' and current_menu == 'text color':
                    font_color = PURPLE
                    show_screen('text color', text_color_list)

                if word_clicked == 'black' and current_menu == 'text color':
                    font_color = BLACK
                    show_screen('text color', text_color_list)

                if word_clicked == 'small' and current_menu == 'window size':
                    width = window_sizes.get('small').get('width')
                    height = window_sizes.get('small').get('height')
                    win = pygame.display.set_mode((width,height))
                    current_window_size = 'small'
                    show_screen('window size', window_size_list)

                if word_clicked == 'medium' and current_menu == 'window size':
                    width = window_sizes.get('medium').get('width')
                    height = window_sizes.get('medium').get('height')
                    win = pygame.display.set_mode((width,height))
                    current_window_size = 'medium'
                    show_screen('window size', window_size_list)

                if word_clicked == 'large' and current_menu == 'window size':
                    width = window_sizes.get('large').get('width')
                    height = window_sizes.get('large').get('height')
                    win = pygame.display.set_mode((width,height))
                    current_window_size = 'large'
                    show_screen('window size', window_size_list)

                



                # if mouse_pos[0]>=70 and mouse_pos[0]<=70+wbox and mouse_pos[1] >=150 and mouse_pos[1]<150+hbox:
                #     win.fill(WHITE)
                #     pygame.time.delay(100)
                #     pygame.display.update()
                #     display_TITLE("Setting")
                #     Menu_function(Setting_list)
                    
                        
                # if mouse_pos[0]>=85 and mouse_pos[0]<=85+wbox and mouse_pos[1] >=260 and mouse_pos[1]<260+hbox:
                #     win.fill(WHITE)
                #     display_TITLE("scoreboard")

                # elif mouse_pos[0]>=85 and mouse_pos[0]<=85+wbox and mouse_pos[1] >=364 and mouse_pos[1]<364+hbox:
                #     win.fill(WHITE)
                #     display_TITLE("escape")
                #     show_main_menu = True
#                 #if mouse_pos[0]>=0 and mouse_pos[0]<=WIDTH and mouse_pos[1] >=0 and mouse_pos[1]<HEIGHT:
#                     #win.fill(WHITE)
#                     #display_TITLE("Screen Size")#WIDTH/2-text.get_width()/2, 70 )
#                     print("("+str(mouse_pos[0])+"," + str(mouse_pos[1])+")")

#instructions
                # if instructions:
                #     myFile=open('instruction.txt', 'r')
                #     yi=150
                #     for line in myfile.readlines():
                #         text=INSTRUCTIONS_FONT.render(line, 1, BLACK)
                #         win.blit(40, yi)
                #         pygame.display.update()
                #         pygame.time.delay(100)
                #         yi+=50
                #     myFile.close()
                #     if xm >335 and xm<459 and ym>745:
                #         Menu_Black()
                #         MAINMENU = True
                #         INSTRUCTIONS = False
                # if SETTINGS:
                #     SettingMenuWin(xm,ym)
pygame.quit()


