#script to find the longest common motif in ~100 1kb sequences
import re
folder = open('rosalind_lcsm.txt', 'r')
str1 = folder.read()
str1 = re.sub(r'\n?>?', '',  str1)
strings = re.split('Rosalind_\d\d\d\d', str1)
strings.remove('')
str0 = strings[0]
longestMotif = (0,'')
washere=0
for j in range(0, (len(str0)-longestMotif[0] + 1)):
    for i in range(j+longestMotif[0], len(str1)):
        testStr = str0[j:i+1]
        goodSoFar = True
        for stri in strings:
            if testStr not in stri:
                goodSoFar = False
                break
        if not goodSoFar:
            washere = washere + 1           
            break
        lenStr=len(testStr)
        if (lenStr> longestMotif[0]):
            longestMotif = (lenStr, testStr)


