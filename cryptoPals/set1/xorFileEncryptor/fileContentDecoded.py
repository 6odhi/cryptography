#!/usr/bin/python -tt

import codecs

#Xor
def xored(x,y):
    return "".join(chr(ord(c)^ord(d))for c,d in zip(x,y))


key = raw_input("Enter the secret key .. for decryption\n")
fileName = raw_input("Enter the file name with encoded string whose content you wish to decrypt ..\n")

with open(fileName, 'r') as f:
    text = f.read()
#key calculation
def finalFun(string1, key):
    finalKey = ''
    i=0
    j=0

    for ele in string1:

        if i < len(string1)+1 and j > len(key)-1:
            j = 0
            finalKey += key[j]
            i+=1
            j+=1

        else:
            if i < len(string1)+1:
                finalKey += key[j]
                j+=1
                i+=1

    return finalKey

#Decoding the hex encoded input to string
tmpString = codecs.decode(text, 'hex')
finalKey = finalFun(tmpString, key)
#Xoring the hex decoded string with the key
print "\n\n"+xored(tmpString, finalKey)

