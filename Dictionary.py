import random

class Dictionary:

    def __init__(self, fname):
        self.words = []
        
        f = open(fname, 'r')
        for line in f: self.words.append(line.strip('\n'))
        f.close()
        
        


    def contains(self, word):
        return self.binSearch(self.words, word, 0, len(self.words)-1)


    def binSearch(self, listi, item, mini, maxi):
        if maxi<mini: return False
        mid = int(mini + (maxi-mini)/2)
        if item<listi[mid]: return self.binSearch(listi, item, mini, mid-1)
        elif item>listi[mid]: return self.binSearch(listi, item, mid+1, maxi)
        elif item==listi[mid]: return True




