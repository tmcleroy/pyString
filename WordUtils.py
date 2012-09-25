import random
import Dictionary
import Tile

from Dictionary import *
from Tile import *

class WordUtils:

    def __init__(self, dictionary):
        self.dictionary = dictionary


    #returns a list of tiles. the tiles make up two complete
    #words, the rand parameter determines whether or not the
    #list is in order or randomly shuffled
    def getTileList(self, size=10, rand=True):
        word_length = size-random.randint(1,(size/2))
        word = self.getRandomWord(word_length)
        filler = self.getRandomWord(size-word_length)
        tile_list = list(word+filler)
        if rand: random.shuffle(tile_list)
        #convert the char list to a Tile list
        for i in range(len(tile_list)):
            tile_list[i] = Tile(tile_list[i], i+1)
        return tile_list
        

    #returns a word of given length at random
    def getRandomWord(self, length=8):
        random.shuffle(self.dictionary.words)
        for word in self.dictionary.words:
            if len(word) == length: return word

    #returns a randomly chosen letter between a and z
    def getRandomLetter(self):
        return chr(random.randint(ord('a'),ord('z')))



#test
#u = WordUtils(Dictionary('dict.txt'))
