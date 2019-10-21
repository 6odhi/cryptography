#!/usr/bin/python -tt

import codecs, sys, time
sys.path.append('../3-Challenge')
sys.path.append('../5-Challenge')
from itertools import combinations
from sol3 import singleXor, letterRatio
from sol5 import xored, finalFun

with open("6.txt", "r") as f:
    text = f.read()
text = codecs.decode(text, 'base64')


def hamming_distance(binary_seq_1, binary_seq_2):
    """Computes the edit distance/Hamming distance between two equal-length strings."""
    assert len(binary_seq_1) == len(binary_seq_2)
    dist = 0

    for bit1, bit2 in zip(binary_seq_1, binary_seq_2):
        diff = ord(bit1) ^ ord(bit2)
        dist += sum([1 for bit in bin(diff) if bit == '1'])

    return dist

def keysizeCalc(text):
    distDict = {}
    possibleTexts = []
    for keySize in range(2,41):
        
        #Getting a list of first 4 groups of keys of each keysize 
        keysizeGroups = [text[size:size+keySize] for size in range(0,len(text),keySize)][:4]
        #Creating every possible pair with 4 keys. Calculating hamming distance 
        distance = 0
        pairs = combinations(keysizeGroups, 2)
        for ele1, ele2 in pairs:
            distance += hamming_distance(ele1, ele2)

        #As there are 6 pairs, calculating average
        averageDistance = distance/6

        #Normalized Hamming Distance
        normalDist = averageDistance/keySize

        #Dictionary with normalized distance for each keySize
        distDict[keySize] = normalDist

    #Getting the best 4 keysize values depending upon the calculated hamming distance
    #sorted function returns a list. Using distDict.get as key for sorting based upon the value or the hamming distance
    possibleKeySize = sorted(distDict, key=distDict.get)[:4]

    max = 0
    finalKeyList = []
    keyString = ''

    for ele in possibleKeySize:

        key = ''
        
        for i in range(ele):
            blocks = ''
            #Creating different blocks of text with 0th, 5th, 10th element and so on. Another block with 1st, 6th, 11th --
            for j in range(i, len(text), ele):
                blocks += text[j]
            
            #SingleXor each block to find most occuring character within the block and then forming key by adding up
            key+=str(singleXor(blocks))
        
        #Creating a list of keystrings
        finalKeyList.append(key)
    #Using letter ratio to find the most optimum keystring     
    for ele in finalKeyList:
        if float(letterRatio(ele)) > max:
            max = float(letterRatio(ele))
            keyString = str(ele)

    print "Final Key is --- "+keyString
    print "Length is --- "+str(len(keyString))
    print "Decoded String is down below \n\n\n\n"
    time.sleep(2)
    print xored(text,finalFun(text, keyString))

keysizeCalc(text)
