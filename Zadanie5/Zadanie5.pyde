class KurekWody():
    ilosc_wcisnietych_pokretel_klasy = 1
    def __init__(self, arg_x, arg_y, arg_r):
        self.obrot = 0
        self.wcisniety = False
        self.x = arg_x
        self.y = arg_y
        self.r = arg_r
    def rysuj(self):
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+90), PI + radians(self.obrot+90), PIE)
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+270), PI + radians(self.obrot+270), PIE)
    def obroc(self, stopnie):
        self.obrot += stopnie
    def wcisnij(self):
        KurekWody.ilosc_wcisnietych_pokretel_klasy *= -1
        self.wcisniety = not self.wcisniety
        if self.wcisniety:
            fill(255,0,0)
        else:
            fill(0,0,255)
            
def setup():
    size(400,400)
    global kurek_z_piekla
    global kurek_z_krainy_lodu
    kurek_z_piekla = KurekWody(width/2-100, height/2, 50)
    kurek_z_krainy_lodu = KurekWody(width/2+100, height/2, 50)
def mouseClicked():
    kurek_z_piekla.wcisnij()
    
    
def mouseWheel(event):
    kurek_z_piekla.obroc(20)
    kurek_z_krainy_lodu.obroc(20)
    print(kurek_z_piekla.obrot)
    print(kurek_z_krainy_lodu.obrot)
    
def draw():
    background(120)
    kurek_z_piekla.rysuj()
    kurek_z_krainy_lodu.rysuj()
    print(KurekWody.ilosc_wcisnietych_pokretel_klasy)
    
#chciałam wykombinować jak ominąć potrzebę zmiany kolorów obiektów osobno jednak przerosło mnie to, 
#nie wiedziałam też już jak wybrnąć z piekielnych kurków
#zostawiam więc kod w takiej formie, zwłaszcza że i tak bardzo spóźniony
    
