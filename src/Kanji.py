'''
Created on August 11th, 2011

@author: zermelozf
'''

class Kanji:

    def __init__(self, literal = '', meanings = [], readings = [], jlptLevel = 0):
        self.literal = literal
        self.meanings = meanings
        self.readings = readings
        self.jlptLevel = jlptLevel
        
    def show(self):
        print self.literal, " ( JLPT", self.jlptLevel, "): "
        for m in self.meanings:
            print m, ",",
        print ""
        for r in self.readings:
            print r, ",",
        print " "
        