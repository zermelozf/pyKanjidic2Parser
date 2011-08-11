'''
Created on August 11th, 2011

@author: zermelozf
'''

from xml.sax.handler import ContentHandler
from Kanji import Kanji
from copy import deepcopy

class ListKanji(ContentHandler):

    def __init__(self, searchElement, searchValue):
        self.searchElement = searchElement
        self.searchValue = searchValue
        self.listOfAcceptedElements = ['literal', 'meaning', 'reading', 'jlpt']
        self.isElement = {'literal':0, 'meaning':0, 'reading':0, 'jlpt':0}
        self.element = {'literal':'', 'meaning':[], 'reading':[], 'jlpt':0}
        self.kanjiList = []
        
    def startElement(self, name, attributes):
        try:
            if name != 'reading' and name != 'meaning':
                self.isElement[name] = 1
            elif name == 'reading' and (attributes.getValue("r_type") == "ja_on" or attributes.getValue("r_type") == "ja_kun"):
                self.isElement[name] = 1
            elif name == 'meaning' and attributes.getLength() == 0:
                self.isElement[name] = 1
        except:
            pass
            
    def characters(self, ch):
        if self.isElement['literal']:
            self.element['literal'] = ch
        if self.isElement['jlpt']:
            self.element['jlpt'] = int(ch)
        if self.isElement['meaning']:
            self.element['meaning'].append(ch)
        if self.isElement['reading']:
            self.element['reading'].append(ch)
            
    def endElement(self,name):
        if name == 'character':
            if self.isCurrentCharacterFit():
                lit = self.element['literal']
                mea = self.element['meaning']
                rea = self.element['reading']
                jlp = self.element['jlpt']
                kanji = Kanji(literal=lit, meaning=mea, reading=rea, jlpt=jlp)
                self.kanjiList.append(deepcopy(kanji))
            self.element['literal'] = ''
            self.element['meaning'] = []
            self.element['reading'] = []
            self.element['jlpt'] = 0
        try:
            self.isElement[name] = 0
        except:
            pass
        
    def isCurrentCharacterFit(self):
        if self.element[self.searchElement] == self.searchValue:
            return 1
        return 0
            
if __name__ == '__main__':
    from xml.sax import make_parser
    
    dict = open("../ressources/kanjidic2")   
    parser = make_parser()
    jlpt = ListKanji('jlpt', 4)
    parser.setContentHandler(jlpt)
    parser.parse(dict)
    for kanji in jlpt.kanjiList:
        kanji.show()
    

        