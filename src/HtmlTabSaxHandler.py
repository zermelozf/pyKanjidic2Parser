'''
Created on 22 sept. 2011

@author: zermelozf
'''
from xml.sax.handler import ContentHandler

class HtmlTabHandler(ContentHandler):

    def __init__(self):
        self.parent_element = None
        self.current_element = None
        self.list = []
        
    def startElement(self, name, attributes):
        self.parent_element = self.current_element
        self.current_element = name      
        if self.current_element == 'tr':
            self.list.append([])
            
    def characters(self, ch):
        if self.current_element == 'a' and self.parent_element == 'td':
            self.list[-1].append(ch)
            
    def endElement(self,name):
        pass
        
            
if __name__ == '__main__':
    from xml.sax import make_parser
    from Kanji import *
    from KanjiListSaxWriters import KanjiListToXmlFile
    
    print "Parsing the tab ... ",
    list = open("../resources/vocab_jlpt_n3_cum.xml")
    #list = open("../resources/vocab_jlpt_n3.xml")    
    parser = make_parser()
    vocab_list = HtmlTabHandler()
    parser.setContentHandler(vocab_list)
    parser.parse(list)
    print "done."
    
    print "Creating Vocab List ... ",
    kanjiList = []
    for entry in vocab_list.list[1:]:
        if len(entry) == 4:
            kanjiList.append(Kanji(literal=entry[0], reading = entry[1], meaning = entry[2].split(','), jlpt = 3))
        elif len(entry) == 3:
            kanjiList.append(Kanji(literal=entry[0], meaning = entry[1].split(','), jlpt = 3))
        else:
            pass
    print "done."
    
    for entry in kanjiList:
        entry.show()
    print "Number of entries: ", len(kanjiList)
    
    print "Copy list list to XML File ...", 
    kl2xml = KanjiListToXmlFile("../resources/JLPT_N3_VOC_CUM.xml")
    #kl2xml = KanjiListToXmlFile("../resources/JLPT_N3_VOC.xml")
    kl2xml.kanjiListToXml(kanjiList)
    print "done."
        