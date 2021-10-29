#ella-rose
#creating window for setting in your game

import pygame, os, random, time

os.system('cls')
pygame.init()

#lists for menu messages
setttingMessages=["Change size","Background", "Object Color"]
#GLOBAL DICTTIONARY
colors = {'red':(150,0,0),'green':(0,200,0),'purple':(150,0,150), 'white':(255,255,255), 'black':(0,0,0)}
WHITE=colors.get('white')
BLACK=colors.get('black')
RED=colors.get('red')

WIDTH=800
HEIGHT=800
wbox=30
hbox=30
x=70
y=150
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Setting Window")

square=pygame.Rect(x,y, wbox, hbox)
#Declare Fonts
TITLE_FONT=pygame.font.SysFont('comicsans', 89)
MENU_FONT=pygame.font.SysFont('comicsans',49)
text= TITLE_FONT.render('message',1,BLACK)

def display_TITLE(message):
    win.fill(WHITE)
    pygame.time.delay(100)
    text= TITLE_FONT.render(message,1,BLACK)
    xm=WIDTH/2-text.get_width()/2
    ym=40
    win.blit(text, (xm,ym))
    pygame.display.update()
    pygame.time.delay(100)

def Menu_function(messages):
    pygame.time.delay(100)
    ym=y
    xm=x+wbox+10
    for i in range(0,len(messages)):
        word=messages[i]
        pygame.draw.rect(win,RED, square)
        text=MENU_FONT.render(word,1,BLACK)
        win.blit(text,(xm,ym))
        pygame.display.flip()
        pygame.time.delay(100)
        ym +=100
        square.y=ym
display_TITLE("Setting")
Menu_function(setttingMessages)
run=True

while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run=False
pygame.quit()
