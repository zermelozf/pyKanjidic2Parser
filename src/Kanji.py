'''
Created on August 11th, 2011

@author: zermelozf
'''

class Kanji:

    def __init__(self, literal = '', meaning = [], reading = [], jlpt = 0, freq = 3000, ref = 3000):
        self.element = {'literal':literal, 'meaning':meaning, 'reading':reading, 'jlpt':jlpt, 'freq':freq, 'ref':ref}
        self.freq = freq
        self.ref = ref
        
    def show(self):
        print self.element['literal'], " ( JLPT", self.element['jlpt'], "): "
        for m in self.element['meaning']:
            print m, ",",
        print ""
        for r in self.element['reading']:
            print r, ",",
        print " "
        print "Freq:", self.element['freq'], "Ref nb:", self.element['ref']
        