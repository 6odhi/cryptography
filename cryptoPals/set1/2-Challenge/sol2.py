#!/usr/bin/python -tt
import codecs

a1 = '1c0111001f010100061a024b53535009181c'
a2 = '686974207468652062756c6c277320657965'

x=codecs.decode(a1, 'hex')
y=codecs.decode(a2, 'hex')

xorString = "".join(chr(ord(c)^ord(d))for c,d in zip(x,y))
#finalStringList = [chr(i) for i in xorList]
#finalString = "".join(finalStringList)

z = codecs.decode('746865206b696420646f6e277420706c6179','hex')

if xorString == z:
    print "Problem solved and xor result is ", xorString



