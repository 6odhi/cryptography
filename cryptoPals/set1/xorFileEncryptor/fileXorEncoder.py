#!/usr/bin/python -tt

"""Program for xor encoding with 3 letter key"""
import codecs

def xored(x,y):
    return "".join(chr(ord(c)^ord(d))for c,d in zip(x,y))

#Input from user for key and file name

key = raw_input("Enter the secret key .. remember this key for decryption in future\n")
fileName = raw_input("Enter the filename whose content you wish to encrypt ..\n")
#Reading file 
with open(fileName,"r") as f: 
    text = f.read()
print "Encoding the below text \n"+text

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


finalKey = finalFun(text, key)
#Print xored, hex Encoded string and storing the same in the file
print codecs.encode(xored(text, finalKey), 'hex')
with open('tmpFile.txt',"w+") as f:
    f.write(codecs.encode(xored(text, finalKey), 'hex'))

print "\n\n\nA file 'tmpFile.txt' has been created as well that stores the encoded file contents \n"
