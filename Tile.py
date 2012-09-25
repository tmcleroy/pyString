import pygame, random
pygame.init()

size = (width, height) = (1280, 720)

class Tile:

    tile_size = 116
    letter_values = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10}
    x_positions = {1:((1/10)*width)-tile_size,
                   2:((2/10)*width)-tile_size,
                   3:((3/10)*width)-tile_size,
                   4:((4/10)*width)-tile_size,
                   5:((5/10)*width)-tile_size,
                   6:((6/10)*width)-tile_size,
                   7:((7/10)*width)-tile_size,
                   8:((8/10)*width)-tile_size,
                   9:((9/10)*width)-tile_size,
                   10:((10/10)*width)-tile_size}

    
    rot_vel = .05

    def __init__(self, letter, xpos):
        self.letter = letter
        self.points = Tile.letter_values[letter]
        self.x = Tile.x_positions[xpos]
        self.y = height + Tile.tile_size + random.randint(-100,400)
        self.angle = random.randint(-30,30)
        #physics
        self.grav = .065
        self.vel = 10

        raw_img = pygame.image.load('img/'+self.letter+'.png')
        self.image = pygame.transform.smoothscale(raw_img,(Tile.tile_size,Tile.tile_size))
        self.image = pygame.transform.rotate(self.image,self.angle)
        self.rect = self.image.get_rect()
        


    def update(self):
        self.vel -= self.grav
        self.y -= self.vel
        


    #this method draws the tile to the screen
    def draw(self, screen):
        self.rect.x, self.rect.y = self.x, self.y
        screen.blit(self.image, self.rect)
