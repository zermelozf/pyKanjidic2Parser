'''
Created on August 10th, 2011

@author: zermelozf
'''
from xml.sax import make_parser
from Kanjidic2SaxHandlers import ListKanji

if __name__ == '__main__':
    dict = open("../ressources/kanjidic2")   
    parser = make_parser()
    jlpt3 = ListKanji('jlpt', 3)
    parser.setContentHandler(jlpt3)
    parser.parse(dict)
    for kanji in jlpt3.kanjiList:
        kanji.show()
    print "JLPT 3 contains", len(jlpt3.kanjiList), "Kanji."