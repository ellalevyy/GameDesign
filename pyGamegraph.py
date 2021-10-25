#ella-rose
#10-20-21`
#mouse position
#drawing reject
#moving object
#K_UP                  up arrow
#K_DOWN                down arrow
#K_RIGHT               right arrow
#K_LEFT                left arrow
#K_INSERT              insert
import os
import pygame as py
import random
 
#first thing
 
py.init()
height= 800
width= 800
 
colors = {'red':(150,0,0),'green':(0,200,0),'purple':(150,0,150), 'white':(255,255,255)}
screen=py.display.set_mode((width,height))  
myColor= colors.get('purple')
color= colors.get('white')
screen.fill(myColor)
py.display.flip()
py.display.set_caption("Moving Square")
 
#parameters to create object square
x=width/2
y=height/2
wbox=50
hbox=50
 
#creating our object square
square=py.Rect(x, y, wbox, hbox)
 
#draw object square
objcolor= colors.get('red')
py.draw.rect(screen, objcolor, square)
py.display.update()

#creating speed to move the object on the screen
speed = 10
 
 #creating a circle
xc=random.randint(10, width)
yc=random.randint(10, height)
radius=wbox/2
center=(xc,yc)
cwidth=xc
surface=screen



#draw the circle
objcolor=colors.get('green')
py.draw.circle(surface, color, center, radius)
py.display.update()



#variable to control the main loop
run=True
while run:
    py.time.delay(100)
    for anyThing in py.event.get():
        if anyThing.type ==py.QUIT:
            run=False
    #To move the square
    keyPressed= py.key.get_pressed()
    if keyPressed[py.K_RIGHT]:
        square.x += speed
    if keyPressed[py.K_LEFT]:
        square.x -= speed
    if keyPressed[py.K_DOWN]:
        square.y += speed
    if keyPressed[py.K_UP]:
        square.y -= speed
    #to move the circle
    if keyPressed[py.K_w]: 
        yc -= speed 
    if keyPressed[py.K_a]:
        xc -= speed
    if keyPressed[py.K_s]:
        yc += speed
    if keyPressed[py.K_d]:
        xc += speed
    #to wrap the square
    if square.x > width:
        square.x = 0    
    if square.x < 0:
        square.x = width

    if square.y > height:
        square.y = 0
    if square.y < 0:
        square.y = height
    #to set boundries on the circle
    if xc > width-radius:
        xc=width-radius
    if xc < 0 + radius:
        xc = 0 + radius
    if yc < 0 + radius:
        yc = 0 + radius
    if yc > height - radius:
        yc = height - radius
    center=(xc,yc)
    
    if square.collidepoint(xc,yc) or square.collidepoint(xc+radius,yc + radius):
        square.x = random.randint(10, width)
        square.y =random.randint(10,height)
        radius += wbox/2
    if radius >= height/3:
        py.quit()
        

    
    
    screen.fill(myColor)
    py.draw.rect(screen, objcolor, square)
    py.draw.circle(surface, color, center, radius)
    py.display.update()
py.quit()



