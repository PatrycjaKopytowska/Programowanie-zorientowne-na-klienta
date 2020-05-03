import random

add_library('pdf')

def setup():
    global img
    global okulary
    global was
    global piorun
    
    size(400, 520)
    
    img = loadImage("Zdjecie do dowodu.jpg")
    
    okulary = loadImage("okulary.png")
    was = loadImage("was.png")
    piorun = loadImage("piorun.png")
    beginRecord(PDF, "portret.pdf")
    
def draw():
    global img
    global okulary
    global was 
    global piorun
    
    image (img, 0, 0, width, height)

    if key == CODED:
        if keyPressed:
            if keyCode == RIGHT:
                image(okulary, 78, 210, width-150, height/4)
                image(piorun, 160, 150, width/5, height/8) #wersja Harry Potter
            elif keyCode == LEFT:
                image(was, 103, 300, width/2, height/4)
            elif keyCode == UP:
                image(okulary, 78, 210, width-150, height/4)
                
    endRecord()
    
def mousePressed():
    exit()
