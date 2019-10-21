#!/usr/bin/python -tt

import codecs, time


encodedStr='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
#Hex decoding and storing the string  
str1 = codecs.decode(encodedStr, 'hex')

outputDict = {}
# http://www.data-compression.com/english.html
CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}


#Function to xor 2 strings of equal length 
def xor(str1, str2):
    return "".join(chr(ord(x)^ord(y)) for x,y in zip(str1, str2))

def singleXor(str1):
    maxOccurs = 0
    finalKey = ''
#Creating a dictionary with key as ascii character and value as xor operation result between key and string 
    for ele in range(1, 256):
        outputDict.update({chr(ele):(xor(str1, chr(ele)*len(str1)))})
    
    
    for key, value in outputDict.items():
#Calculating the final key by adding up the character frequency of each character within the xored string. 
        if float(letterRatio(outputDict[key])) > maxOccurs:
            maxOccurs = float(letterRatio(outputDict[key]))
            finalKey = key
    if finalKey:
        #print outputDict[finalKey], "\nKey is "+finalKey
        return finalKey

def letterRatio(str1):
    numberOfLetters = sum([CHARACTER_FREQ[ele] for ele in str1 if ele in CHARACTER_FREQ])
    return numberOfLetters


print singleXor(str1)
