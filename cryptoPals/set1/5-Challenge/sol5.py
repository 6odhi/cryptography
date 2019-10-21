#!/usr/bin/python -tt
import codecs

def xored(x,y):
    return "".join(chr(ord(c)^ord(d))for c,d in zip(x,y))

#Calculating the finalkey depending upon the string length.
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
text = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = 'ICE'

finalKey = finalFun(text, key)
#remain=len(text)%len(key)
#tmpKeyLength=len(text)/len(key)
#finalKey = key*tmpKeyLength + edit(remain,key)

if codecs.encode(xored(text, finalKey), 'hex') == '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f':
    print "Challenge Solved"

print codecs.encode(xored(text, finalKey), 'hex')
