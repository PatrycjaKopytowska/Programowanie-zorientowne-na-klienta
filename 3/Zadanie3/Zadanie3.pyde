def setup():
    size(500, 500)
    textSize(150)
def draw():
    clear()
    text("P", width/2-70, height/2-50)
    fill(255, 255, 0)
    if key == CODED:
        if keyPressed:
            if keyCode == RIGHT:
                fill(205, 104, 104)
    if keyPressed:
        if key == "k":
            fill(205, 104, 104)
    text("K", width/2, height/2-50)
    fill(57, 204, 204)
    if hex(get(mouseX, mouseY)) != "FF000000" and hex(get(mouseX, mouseY)) != "FFFFFF00" :
        fill(205, 104, 104)
        
    print(hex(get(mouseX, mouseY)))
    
    
    if key == CODED:
        if keyPressed:
            if keyCode == LEFT:
                fill(205, 104, 104)            
    s = createShape()
    s.beginShape()
    s.fill(0,205, 104, 104)
    s.stroke(0,205, 104, 104)
    s.vertex(100, height/4*3)
    s.vertex(200, height/6)
    s.vertex(width/2, height/4*3)
    s.vertex(300, height/6)
    s.vertex(400, height/4*3)
    s.endShape(CLOSE)
    shape(s, 25, 25)

  # 1,75
  # przy zaznaczeniu p i strzałce w prawo powinno się odznaczyć p (przy jednoczesnym zaznaczeniu k, co działa)
  # same strzałki nie powinny diząłać, miały przenosić już istniejące zaznaczenie
