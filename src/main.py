'''
Created on August 10th, 2011

@author: zermelozf
'''
from xml.sax import make_parser
from Kanjidic2SaxHandlers import ListKanji
from KanjiListSaxWriters import KanjiListToXmlFile

if __name__ == '__main__':
    '''
    This script uses the ListKanji class to create a customized list of Kanji from Kanjidic2.
    The list is then saved to an XML file.
    You need to put the Kanjidic2 file available at http://www.csse.monash.edu.au/~jwb/kanjidic2/ 
    in the resources directory.
    '''
    #Create a customized list of JLPT3 Kanji
    dict = open("../resources/kanjidic2")  
    print "Creating the list ...", 
    parser = make_parser()
    jlpt3 = ListKanji('jlpt', 3)
    parser.setContentHandler(jlpt3)
    parser.parse(dict)
    print "done."
    for kanji in jlpt3.kanjiList:
        kanji.show()
    print "JLPT 3 contains", len(jlpt3.kanjiList), "Kanji."
    
    #Save the list to an XML file
    print "Copy JLPT3 list to XML File ...", 
    kl2xml = KanjiListToXmlFile("../resources/JLPT3.xml")
    kl2xml.kanjiListToXml(jlpt3.kanjiList)
    print "done."