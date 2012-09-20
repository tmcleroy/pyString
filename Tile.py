import pygame

class Tile:

    letter_values = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10}

    def __init__(self, letter):
        self.letter = letter
        self.points = Tile.letter_values[letter]
        self.x = 0
        self.y = 0

       #self.surface = pygame.image.load('img/'+self.letter+'.png')
        
