from util.entities import *
from util.test import *
def printout(sentence,opfile):
    keyFile = open(opfile, 'a')
    for i in range(len(sentence.pos)):
        keyFile.write(sentence.words[i]+"\t"+sentence.pos[i]+"\n")
    keyFile.write("\n")
    keyFile.close()

def parseTraining (keyFileName,c):
    keyFile = open(keyFileName, 'r')

    keyTokenPrev="null"
    keyPosPrev="null"
    i=0
    for key in keyFile:
        i+=1
        if(i%100000)==0:
            print("On line ",i)
        key = key.rstrip('\n')
        keyFields = key.split('\t')
        if(len(keyFields)==2):
            keyToken = keyFields[0]
            keyPos = keyFields[1]
            #print("Adding "+keyToken+" to "+keyPos)
            if keyTokenPrev!="null":
                #print("Adding word ", keyToken)
                c.addWordArc(keyTokenPrev,keyPosPrev,keyPos)
            keyTokenPrev=keyToken
            keyPosPrev=keyPos
        else:

            if keyTokenPrev!="null":
                #print("Adding word ", keyToken)
                c.addWord(keyTokenPrev,keyPosPrev)
            keyTokenPrev="null"
            keyPosPrev="null"
def parseDev(keyFileName,c,opfile):
    keyFile = open(keyFileName, 'r')
    key = keyFile.read()
    lines=key.split("\n\n")
    j=0
    for line in lines:
        i = 0
        words=line.split()
        if len(words)>1:
            for word in words:
               if(i==0):
                   i=1
                   s=Sentence()
                   s.addToken(word)
               else:
                   s.addToken(word)
        #s.printout()
            maxs= c.viterbi(s)
            printout(maxs,opfile)
        j+=1
        if(j%1000)==0:
            print("On sentence ",j)
'''c=Corpus()
parseTraining("/home/user/Documents/Course_Books/NLP/hw4/train_corp",c)
#c.printout()
parseDev("/home/user/Documents/Course_Books/NLP/hw4/dev_corp",c,"/home/user/Documents/Course_Books/NLP/hw4/dev_corp_op")
score("/home/user/Documents/Course_Books/NLP/hw4/dev_corp_op","/home/user/Documents/Course_Books/NLP/hw4/dev_corp_op1")

'''
c=Corpus()
parseTraining("/home/user/Documents/Course_Books/NLP/hw4/WSJ_POS_CORPUS_FOR_STUDENTS/WSJ_02-21.pos",c)
#c.printout()
parseDev("/home/user/Documents/Course_Books/NLP/hw4/WSJ_POS_CORPUS_FOR_STUDENTS/WSJ_24.words",c,"/home/user/Documents/Course_Books/NLP/hw4/WSJ_POS_CORPUS_FOR_STUDENTS/WSJ_24_op")
score("/home/user/Documents/Course_Books/NLP/hw4/WSJ_POS_CORPUS_FOR_STUDENTS/WSJ_24_op","/home/user/Documents/Course_Books/NLP/hw4/WSJ_POS_CORPUS_FOR_STUDENTS/WSJ_24.pos")