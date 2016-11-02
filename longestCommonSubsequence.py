import re

file = open('dna7.txt')

test = file.read()


test = re.split(r'Rosalind_', test)
for i in range(len(test)):
    test[i] = re.sub(r'\n|>|\d', '', test[i])
print(test)
string1 = test[-1]
string2 = test[-2]



startList = [ [[] for x in range(len(string2) +1)] for x in range(len(string1) + 1)]
print(startList[0][3])

for i in range(len(string1) ):
    for j in range(len(string2)):
        if string1[i] == string2[j]:
            startList[i+1][j+1]= startList[i][j] + [string1[i]]
        else:
            if len(startList[i+1][j]) > len(startList[i][j+1]):
                startList[i+1][j+1] = startList[i+1][j]
            else:
                startList[i+1][j+1] = startList[i][j+1]

ans = startList[-1][-1]
for s in ans:
    print(s, end = '')
print(' ')

#use this helper to find the shortest common supersequence, using the longest common subsequence
def interleave(string1, string2, lcs):
    if len(lcs) == 0:
        result = string1 + string2
    else:
        common = lcs[0]
        index1 = string1.index(common)
        index2 = string2.index(common)
        result = string1[:index1] + string2[:index2] + common + interleave(string1[index1 + 1:], string2[index2+1:], lcs[1:])

    return result
