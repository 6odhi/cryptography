#!/usr/bin/python -tt

import codecs

encodedList = []
with open('4.txt', 'r') as f:
    encodedList = [line.rstrip() for line in f]

ascii_text_chars = list(range(97, 123)) + list(range(65, 81)) + [32]

def letter_occurence(inputString):
    return sum([ord(ele) in ascii_text_chars for ele in inputString])

#def probable_text(inputString):
#    r = letter_ratio(inputString)
#    print r
#    if r>0.7:

#        return True
#    else:
#        return False
    
#Check with a sample text

def xored(x,y):
    return "".join(chr(ord(c)^ord(d))for c,d in zip(x,y))

def finalFunc(encodedString):
    best = None
    for sample in encodedString:
        decodedSample = codecs.decode(sample, 'hex')
        for ele in range(1,256):
            xoredString = xored(decodedSample, chr(ele)*len(decodedSample))
            letterNos = letter_occurence(xoredString)

            if best == None or letterNos > best['number_of_letters']:
                best = {'encodedString':decodedSample, 'finalString':xoredString, 'number_of_letters':letterNos ,'key':chr(ele)}
    return best

print finalFunc(encodedList)

