#!/usr/bin/python -tt
from Crypto.Cipher import AES
import codecs

key="YELLOW SUBMARINE"

with open("7.txt", "r+") as f:
    text = f.read()
cipher = codecs.decode(text, 'base64')

obj = AES.new(key, AES.MODE_ECB)
decodedText = obj.decrypt(cipher)


print decodedText
