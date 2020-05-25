def setup():
    size(400,400)
    rectMode(CORNER)
    fill(255,179,179) # lepiej raz niż co klatkę
def draw():
    print(('wymiary okna: {}, {}').format(width, height))
    print(mouseX, mouseY, mousePressed)
    rect(150, 150, width/4, width/4, 20)
    if mousePressed:
        line(mouseX, mouseY, mouseX, mouseY) 
    else: 
        line(mouseX, mouseX, mouseX, mouseY)
        stroke(2, 63, 0)

# 2pkt
