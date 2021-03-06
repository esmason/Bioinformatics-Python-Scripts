from bioDecorators import fastaReader

@fastaReader
def find_alignment(fasta_list):
    string1 = fasta_list[0][1]
    string2 = fasta_list[1][1]
    #init 'soln so far' tables
    distTable = [[None for x in range(len(string2) +1)] for x in range(len(string1)+1)]
    strTable = [[None for x in range(len(string2) +1)] for x in range(len(string1)+1)]
    #numOp[i][j] contains number of optimal alignment options  (mod 134217727 ) for string1[:i-1] string2[:j-1]

    numOps = [[0 for x in range(len(string2) +1)] for x in range(len(string1)+1)]


    for i in range(len(string1)+1):
        
        for j in range(len(string2)+1):
            if i == 0 or j == 0:
                distTable[i][j] = max(i, j)
                strTable[i][j] = ('','')
                numOps[i][j] = 1

            else:
                minval = min(distTable[i-1][j], distTable[i][j-1], distTable[i-1][j-1]) + 1
                if distTable[i-1][j-1] + 1 == minval:
                    if string1[i-1] == string2[j-1]:
                        minval -=1
                    strTable[i][j] = (strTable[i-1][j-1][0] + string1[i-1] , strTable[i-1][j-1][1] + string2[j-1])
                    numOps[i][j] = numOps[i-1][j-1]
                elif distTable[i-1][j-1] == minval:
                    if string1[i-1] == string2[j-1]:
                        strTable[i][j] = (strTable[i-1][j-1][0] + string1[i-1] , strTable[i-1][j-1][1] + string2[j-1])
                        numOps[i][j] = numOps[i-1][j-1]
                if distTable[i][j-1] + 1== minval:
                    strTable[i][j] = (strTable[i][j-1][0]+ '-', strTable[i][j-1][1] + string2[j-1])
                    numOps[i][j] += numOps[i][j-1] % 134217727

                if distTable[i-1][j] + 1== minval:
                    strTable[i][j] = (strTable[i-1][j][0] + string1[i-1], strTable[i-1][j][1] + '-')
                    numOps[i][j] += numOps[i-1][j] % 134217727
                distTable[i][j] = minval


    distance = distTable[len(string1)][len(string2)]


    alignment = [ strTable[len(string1)][len(string2)][0],
              strTable[len(string1)][len(string2)][1]  ]

    ops = numOps[len(string1)][len(string2)] % 134217727
    return(distance, alignment, ops)


