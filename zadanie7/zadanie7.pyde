from abc import ABCMeta, abstractmethod
class Pet():
    __metaclass__=ABCMeta
    @abstractmethod
    def speak(self):
        super().__init__()
        return 'no sound'
class Cat(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('meow', random(50, width-70), random(50, height-50))
        return 'meow'
class Panda(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('rawr', random(50, width-70), random(50, height-50))
        return 'rawr'
class Dog(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('woof', random(50, width-70), random(50, height-50))
        return 'woof'
    def gimmePaw(self):
        image(loadImage("lapa.png"), random(50, width-70), random(50, height-100))
    def __sub__(self, other):
        return self.name[0]+ ' i ' + other.name[0]
class Bunny(Pet):
    pass
    
def setup():
    size(400,400)
    textSize(20)
    rex = Dog('Rex')
    benio = Dog('Benio')
    skrypcik = Cat('Skrypcik')
    Kliford = Dog('Kliford')
    # a gdzie panda? ;)
    global list_of_pets
    list_of_pets = [rex, benio, skrypcik, Kliford]
    print(isinstance(skrypcik, Pet))
    print(rex-benio)

def draw():
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak()
        if isinstance(pet, Dog):
            pet.gimmePaw()
            
# 1,25pkt
