'''
Created on August 11th, 2011

@author: zermelozf
'''

from xml.sax.saxutils import XMLGenerator

class KanjiListToXmlFile:

    def __init__(self, filepath):
        self.file = open(filepath, "w+")
        self.handler = XMLGenerator(self.file, 'utf-8')
        self.handler.startDocument()
        
    def __del__(self):
        self.handler.endDocument()
        
    def kanjiToXml(self, kanji):
        self.handler.startElement('character', {})
        for el in kanji.element:
            if isinstance(kanji.element[el], unicode):
                self.handler.startElement(el, {})
                self.handler.characters(kanji.element[el])
                self.handler.endElement(el)
            elif isinstance(kanji.element[el], int):
                self.handler.startElement(el, {})
                self.handler.characters(str(kanji.element[el]))
                self.handler.endElement(el)
            elif isinstance(kanji.element[el], list):
                for m in kanji.element[el]:
                    self.handler.startElement(el, {})
                    self.handler.characters(m)
                    self.handler.endElement(el)
        self.handler.endElement('character')
    
    def kanjiListToXml(self, kanjiList):
        for kanji in kanjiList:
            self.kanjiToXml(kanji)
            
        
        
        