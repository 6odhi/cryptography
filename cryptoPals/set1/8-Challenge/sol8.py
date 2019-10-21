#!/usr/bin/python -tt
import codecs, time, string, sys

with open("8.txt", "r+") as f:
    textList = f.readlines()
#Storing each cipher text in a list while striping the new lines
textList = [text.strip() for text in textList]
newDict = {}
counter = 0
    
block = ''
blockList = []

#Adding 16bytes block for each text in a list
for text in textList:
    for counter in range(0, len(text), 16):
        block = text[counter:counter+16]
        blockList.append(block)
    #Checking if there're common elements in the block list. Adding the count of unique elements into a dictionary along with the actual cipher
    #The cipher with minimum count will be the answer. set() is used for removing redundancy within the list elements
    if len(blockList) != len(set(blockList)):
        count = len(set(blockList))
        newDict[count] = text

    blockList = []
#Checking the cipher with min count and printing the same
cipherKey = min(newDict.keys())
print newDict[cipherKey]


    
