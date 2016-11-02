import re
def consensus(file):
#read file
    folder = open(file, 'r')
    raw = folder.read()
    #remove names, line breaks
    seqs1 = re.split('\n?>Rosalind_\d\d\d\d\n',  raw)
    seqs1.remove('')
    seqs = []
    for seq in seqs1:
        seq = seq.replace("\n", '')
        seqs.append(seq)

                     
    firstSeq = seqs[0]
    #init profile "matrix"
    numA= [0] * len(firstSeq)
    numC= [0] * len(firstSeq)
    numG= [0] * len(firstSeq)
    numT= [0] * len(firstSeq)
    #count number of times a base occurs at each position for each seq, record in profile "matrix"
    for seq in seqs:
        for i in range(len(firstSeq)):
            if (seq[i] == "A"):
                numA[i] = numA[i] +1
            elif (seq[i] == "C"):
                numC[i] = numC[i] +1
            elif (seq[i] == "G"):
                numG[i] = numG[i] +1
            elif (seq[i] == "T"):
                numT[i] = numT[i] +1
    #initialize consesus sequence
    consensus = ''
    #construct consensus seq
    for i in range(len(firstSeq)):
        if (max(numA[i], numC[i], numG[i], numT[i])== numA[i]):
            consensus += "A"
        elif (max(numA[i], numC[i], numG[i], numT[i])== numG[i]):
            consensus += "G"
        elif (max(numA[i], numC[i], numG[i], numT[i])== numT[i]):
            consensus += "T"
        else:
            consensus += "C"

    #format return to conform with answer specs           
    print(consensus)
    print("A: ", end='')
    strA=str(numA)
    strA=strA.replace(']', '')
    strA=strA.replace('[', '')
    strA=strA.replace(',', '')
    print(strA)
    
    print("C: ", end='')
    strC=str(numC)
    strC=strC.replace(']', '')
    strC=strC.replace('[', '')
    strC=strC.replace(',', '')
    print(strC)    
 

    print("G: ", end='')
    strG=str(numG)
    strG=strG.replace(']', '')
    strG=strG.replace('[', '')
    strG=strG.replace(',', '')
    print(strG)  

    print("T: ", end='')
    strT=str(numT)
    strT=strT.replace(']', '')
    strT=strT.replace('[', '')
    strT=strT.replace(',', '')
    print(strT)





    return 



