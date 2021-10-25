import pygame, os, time
#Ella-Rose Levy
#learning how to use pygame

pygame.init()
#declear the object to display game
#red = (255,0,0)
#purple(150,0,150)
#create a dictionary of colors
#ask the user the size and color for the window

colorChoices = {'red':(150,0,0),'green':(0,200,0),'purple':(150,0,150)}
colors=input("what colors would you like for the window? purple, green, or red?")

check = True

while check: 
    height= input("enter the height of your window?")
    width= input("What is the width of you window")  
    myColor= colorChoices.get(colors)
    height=int(height)
    width=int(width)
    screen=pygame.display.set_mode((width,height))
#screen=pygame.display.set_mode((width,height))
#myColor= colors.get(colors)
    check=True

    try:
        height=int(height)
        width=int(width)
        if height>100 and width>100 and height<1200 and width<12000:
            check=False
        else:
            print("sorry this value is not between 100-1200")
    except ValueError: 
        print("Sorry enter a valid number")


screen.fill(myColor)
pygame.display.update() #Use to update your screen

#add a title
pygame.display.set_caption("My Game")
run=True #variable to control the main loop

while run:
    pygame.time.delay(1000) #milliseconds
    for anything in pygame.event.get():
        if anything.type == pygame.QUIT:
            run =False
pygame.quit() 
