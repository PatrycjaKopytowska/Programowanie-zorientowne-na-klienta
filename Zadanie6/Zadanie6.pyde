class Kwadrat():
    def __init__(self, bok): # konstruktor jak się dowiedzieliśmy jest metodą prywatną, nie można go wywołać na obiekcie klasy po kropce, ani po za klasą
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)

        
class KolorowyKwadrat(Kwadrat): # dziedziczymy po klasie Kwadrat aby móć skorzystać z jej funkcjonalności
    def sketchKolorowy(self, x, y):
        Kwadrat.sketch(self, x, y) # korzystamy z metody klasy bazowej:
        fill(255, 153, 153) # wypadałoby zapamiętać kolor sprzed zmiany i przywrócić go po narysowaniu, bo obecnie, wszystko narysowane po tym kolorowymkwadracie będzie w tym kolorze
        
def setup():
    size(500, 500)
    malyKwadrat = Kwadrat(50.0) 
    malyKwadrat.sketch(220, 250)
    malyKwadrat = Kwadrat(50.0) 
    malyKwadrat.sketch(220, 300)
    malyKolorowyKwadrat = KolorowyKwadrat(50.0)
    malyKolorowyKwadrat.sketchKolorowy(220, 200)
    malyKolorowyKwadrat = KolorowyKwadrat(30.0)
    malyKolorowyKwadrat.sketchKolorowy(230, 210)
    malyKolorowyKwadrat = KolorowyKwadrat(30.0)
    malyKolorowyKwadrat.sketchKolorowy(230, 310)

# plus do aktywności za zabawę w ustawianie ;)
# 1,75pkt
