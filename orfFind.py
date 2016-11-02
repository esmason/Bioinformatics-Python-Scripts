bases = ['U', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
proteins = ['F', 'F', 'L', 'L', 'S', 'S','S','S', 'Y', 'Y', 'Stop', 'Stop', 'C',
            'C', 'Stop', 'W', 'L', 'L', 'L','L', 'P','P','P','P','H','H','Q','Q',
            'R','R','R','R','I','I','I', 'M','T','T','T','T','N', 'N', 'K', 'K','S','S','R',
            'R','V','V','V','V','A','A','A','A','D','D','E','E', 'G', 'G', 'G', 'G']
codonDict = dict(zip(codons, proteins))

def rev_comp(dna):
    rev_comp = ''
    keys = 'ACTG'
    vals = 'TGAC'
    rev_letters = dict(zip(keys,vals))
    for c in dna:
        rev_comp += rev_letters[c]
    return rev_comp



    

#finds ORFs in one direction from an RNA transcript
def findOrfRNA(rna):
    #init list of ORFs to return
    listORF = []
    for i in range(3):
        print(i)
        #keeps track of whether we've started an ORF
        orfStarted = False
        #init string that holds current ORF sequence to add to list when terminated
        tempStr = ''
        for j in range(i, len(rna), 3):
            if ((j+3)>(len(rna))):
                tempStr = ''
                break
            #amino acid of this particular codon
            codon = rna[j:3+j]
            aa=codonDict[codon]
            if (aa == 'M'):
                orfStarted = True
            elif (aa == 'Stop'):
                orfStarted = False
                #adds ORF to list of orfs 
                if (len(tempStr)>0):
                    for i in range(len(tempStr)):
                        if tempStr[i] == 'M':
                            listORF.append(tempStr[i:])
                tempStr = ''
            if (orfStarted):
                tempStr = tempStr + aa
    return listORF

#finds forward and reverse of ORF from dna sequence
def findOrfDNA(dna):
    dnaseq=dna
    dnaseq2 = revComp(dnaseq)
    rnaseq = dnaseq.replace( 'T', 'U')
    rnaseq2 = dnaseq2.replace( 'T', 'U')
    lstORF1 = findOrfRNA(rnaseq)
    lstORF2 = findOrfRNA(rnaseq2)
    for i in lstORF2:
        if i not in lstORF1:
            lstORF1.append(i)
    return lstORF1

def main(file):
    folder = open(file, 'r')
    dna = folder.read()
    dna2 = dna.replace('\n', '')
    orfs= findOrfDNA(dna2)
    for i in orfs:
        print(i)
    



            
                


