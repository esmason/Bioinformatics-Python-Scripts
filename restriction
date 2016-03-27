

import re


def revComp(dna):
    revComp = ''
    for char in dna:
        rev=''
        if char == 'A':
            rev = 'T'
        elif char == 'T':
            rev = 'A'
        elif char == 'G':
            rev = 'C'
        elif char == 'C':
            rev = 'G'
        revComp = rev + revComp
    return revComp


file = open('dna7.txt', 'r')
folder = file.read()

dna = re.sub(r'\n', '' , folder)

ans = []
print(dna)
for i in range(len(dna)-3):
    if dna[i:i+4] == revComp(dna[i:i+4]):
        ans.append((i+1, 4))
for i in range(len(dna)-5):

    if dna[i:i+6] == revComp(dna[i:i+6]):
        ans.append((i+1, 6))
for i in range(len(dna)-7):
    if dna[i:i+8] == revComp(dna[i:i+8]):
        ans.append((i+1, 8))
for i in range(len(dna)-9):
    if dna[i:i+10] == revComp(dna[i:i+10]):
        ans.append((i+1, 10))
for i in range(len(dna)-11):
    if dna[i:i+12] == revComp(dna[i:i+12]):
        ans.append((i+1, 12))
print(ans)

for e in ans:
    print(str(e[0]) +" " + str(e[1]))

