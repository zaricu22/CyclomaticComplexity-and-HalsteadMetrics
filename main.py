import math
from chars import *
import sys
import os

def scanFileORDirectory(path):
    # path_of_the_directory= "C:\\Users\UROS\Documents\project-builder\CBuilder\C\izdvojeni'
    print("\nFilename: uniqOprts uniqOprnds totalOprts totalOprnds  Length  Vocab  Volume  Diff Effort Time Bug  ccCount\n")
    if (os.path.isfile(path)):
        manageFile(path)
    else:
        for filename in os.listdir(path):
            f = os.path.join(path,filename)
            if os.path.isfile(f):
                print(filename+":  ", end = '')
                manageFile(path+"\\"+filename)

def manageFile(filepath):
    file = open(filepath, 'r')
    splits = []
    word = ''
    opr =''
    codeBox = ''

    for line in file:  
        for char in line:
            codeBox += char        
            if (char in separators) :
                if(word):
                    splits.append(word)
                if(opr):
                    splits.append(opr)
                    opr = ''
                word = ''
            elif(char in opers and char in doubleOpers): #check for ++ or += or ....
                if(word):
                    splits.append(word)
                opr += char
                word = ''
            elif(char in opers):
                if(word):
                    splits.append(word)
                splits.append(char)
                word = ''
            else:
                if(opr):
                    splits.append(opr)
                    opr = ''
                word += char

    operators = {}
    operands = {}

    for index in splits:
        if(index in keyWords or index in opers):
            if(index in operators):
                count = operators[index]
                count += 1
                operators[index] = count
            else:
                operators[index] = 1
        else:
            if(index in operands):
                count = operands[index]
                count += 1
                operands[index] = count
            else:
                operands[index] = 1

    smallN1 = 0
    capitalN1 = 0
    smallN2 = 0
    capitalN2 = 0
    temp = 0

    for n in operators:
        capitalN1 += operators[n]
        smallN1 += 1

    for n in operands:
        capitalN2 += operands[n]
        smallN2 += 1

    ccCount = 1

    for n in operators:
        if(n in loopWords):
            ccCount += operators[n]


    progLength = capitalN1 + capitalN2
    progVocab = smallN1 + smallN2
    estimatedLength = (smallN1 * math.log2(smallN1)) + (smallN2 * math.log2(smallN2))
    purityRatio = estimatedLength / progLength
    volume = estimatedLength * math.log2(progVocab)
    difficulty = (smallN1 / 2) * (capitalN2 / smallN2)
    progEffort = difficulty * volume
    progTime = progEffort / 18
    deliveredBug = volume / 3000

    results = {'n1': smallN1, 'N1': capitalN1, 'n2': smallN2, 'N2':capitalN2, 'progLength': progLength, 'progVocab':progVocab,
                'estimatedLength': estimatedLength, 'purityRatio': purityRatio, 'volume': volume, 'difficulty': difficulty,
                'progEffort': progEffort, 'progTime': progTime, 'deliveredBug': deliveredBug, 'codeBox': codeBox, 'ccCount': ccCount}

    file.close()

    print(str(smallN1)+
             ' '+str(smallN2)+
             ' '+str(capitalN1)+
             ' '+str(capitalN2)+
             ' '+str(progLength)+
             ' '+str(progVocab),
             ' '+str("{:.2f}".format(volume))+
             ' '+str("{:.2f}".format(difficulty))+
             ' '+str("{:.2f}".format(progEffort))+
             ' '+str("{:.2f}".format(progTime))+
             ' '+str("{:.2f}".format(deliveredBug))+
             ' '+str(ccCount))

    return results

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
