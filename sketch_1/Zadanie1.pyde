def setup():
    size(400,400)
    rectMode(CORNER)
def draw():
    print(('wymiary okna: {}, {}').format(width, height))
    print(mouseX, mouseY, mousePressed)
    fill(255,179,179);
    rect(150, 150, width/4, width/4, 20);
    if mousePressed:
        line(mouseX, mouseY, mouseX, mouseY) 
    else: 
        line(mouseX, mouseX, mouseX, mouseY)
        stroke(2, 63, 0)
