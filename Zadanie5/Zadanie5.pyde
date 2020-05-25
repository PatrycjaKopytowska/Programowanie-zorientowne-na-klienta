class KurekWody():
    def __init__(self, arg_x, arg_y, arg_r, czyCieply): # dzieki temu, że przekazany jako argument może być różny na starcie
        self.obrot = 0
        self.wcisniety = czyCieply # teraz jest argumentem instancji nie klasy, więc jest zapamiętywany dla każdego obiektu oddzielnie
        self.x = arg_x
        self.y = arg_y
        self.r = arg_r
    def rysuj(self):
        if self.wcisniety:
            fill(255,0,0)
        else:
            fill(0,0,255)
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+90), PI + radians(self.obrot+90), PIE)
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+270), PI + radians(self.obrot+270), PIE)
          
    def obroc(self, stopnie):
        self.obrot += stopnie
    def wcisnij(self):
        self.wcisniety = not self.wcisniety
            
def setup():
    size(400,400)
    global kurek_z_piekla
    global kurek_z_krainy_lodu
    kurek_z_piekla = KurekWody(width/2-100, height/2, 50, True)
    kurek_z_krainy_lodu = KurekWody(width/2+100, height/2, 50, False)
    
def mouseClicked():
    if mouseX<width/2:
        kurek_z_piekla.wcisnij()
    else:
        kurek_z_krainy_lodu.wcisnij()
    
    
def mouseWheel(event):
    kurek_z_piekla.obroc(20)
    kurek_z_krainy_lodu.obroc(20)
    print(kurek_z_piekla.obrot)
    print(kurek_z_krainy_lodu.obrot)
    
def draw():
    background(120)
    kurek_z_piekla.rysuj()
    kurek_z_krainy_lodu.rysuj()
    
#0,75pkt 
# liczył się pomysł na klasę, ale też na atrybuty i metody, a te zostały jak u mnie w kodzie, więc nie mogę za nie zapunktować
# nie jestem pewna, co chciałaś osiągnąć, ale w jakiś sposób naprawiłam, sprawdź, może o to chodziło  
