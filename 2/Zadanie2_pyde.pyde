def setup():
    size(300, 300)
    frameRate(100)                     
    global slownik_kolorow    
                    
    global x
    global y
    x = 0  
    y = height/2     
                                                              
    slownik_kolorow = {"różowy":(255, 153, 153), "niebieski":(102, 179, 255), "zielony":(170, 255, 128)} 
    global lista_kolorow
    lista_kolorow = []
                                      
    for klucz, wartosc in slownik_kolorow.items():
        lista_kolorow.append(wartosc) 
    
    global iteracja_programu
    iteracja_programu = 0            

def draw():  
    
    
    global x
    global y
          
    background (255, 230, 204)
                      
    global iteracja_programu
    iteracja_programu +=1
                                     
    stroke(0,0,255,80)                
    stroke(*slownik_kolorow["niebieski"]) 
                       
    x+=1
    y+=1
                        
    fill(*lista_kolorow[iteracja_programu/150%len(lista_kolorow)])
    circle(x,y,30)

    if x > width/2 and y > height/2:
        y -= 2
    
    if x > width/2 and y < height/2:
        x -= 2
        y -= 2
    if x < width/2 and y < height/2:
        x -= 2
    
    if mousePressed:
        exit()
