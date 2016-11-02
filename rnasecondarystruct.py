#calculate number of valid ssRNA secondary structures using dynamic programming, assuming the only constraint is no cross-bridging
#based on catalan number recurrence relation


rna = 'UUGUACCGCAUGCGUAUAACGGCCGCGUAUCGAAGCUCGAACUAUAUUGCAUAUAAUUAACGCGGCUAUAAAUUUAAUUGGGUACCCGUAGCAUCUAAUUAGCACGUUUAAAUAAUCCCGCGCGGCGUUAUAAGAAUUGCAAAAGCUUCAAUUGUUGCCUAGAUUAUAUCACGUGACCGGUAAUUAUCGGCCGCGAUAGCGAUUUUCGCAUGCGAGCUAUACGAUCAUGAAGAUCUAUAGUUAUACGCCGGACGCUGC'
#initialize indices of all bases
A, U, C, G = [ [1 if rna[x]==s else 0 for x in range(len(rna)) ]  for s in "AUCG"]

#initialize table where D(i,j) is the catalan number in the rna string from i to j inclusive
D = [ [ None for x in range(len(rna))] for x in range(len(rna))]


def rna_catalan(i, j):
   
    if i>j:
        return 1
    elif i==j or (i - j) % 2 == 0 or not sum(U[i:j+1]) == sum(A[i:j +1]) or not sum(G[i:j+1]) == sum(C[i:j +1]):
        D[i][j] = 0
    elif j-i == 1 and ( (sum(U[i:j+1]) == 1 and sum(A[i:j +1]) ==1) or  (sum(G[i:j+1]) == 1 and sum(C[i:j +1]) ==1)):
        D[i][j] = 1
    elif D[i][j] == None:
        D[i][j] = sum([rna_catalan(i+1,x-1)*rna_catalan(x+1, j)*is_valid(i,x) for x in range(i+1, j+1)])
    return D[i][j]


letterDict = dict(zip('AUCG', 'UAGC'))
def is_valid(i , j):
    if rna[i] == letterDict[rna[j] ]:
        return 1
    else:
        return 0
print(rna_catalan(0,len(rna)-1))
