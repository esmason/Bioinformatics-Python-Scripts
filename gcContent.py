#returns a tuple with the max gc Content % of a file with FASTA seqs and the name of the sequence
def gcContent(file):
    folder = open(file , 'r')
    read_file = folder.read()
    fasta= read_file.split('>')
    #print(fasta)
    maxGc = (0.0, 'starter')
    for seq in fasta:
        gc = 0.0
        total = 0.0
        for char in seq:
            if ((char == 'A') or (char=='T')):
                total = 1.0 + total
            if ((char == 'C') or (char=='G')) :
                gc = 1.0 + gc
                total = 1.0 + total
        if total == 0.0:
            total = 1


        #print(gc)
        #print(total)
        gc_content = gc/total
       
        if (gc_content*100 > maxGc[0]):
            maxGc = (gc_content*100, seq[0:13])    
    return maxGc
