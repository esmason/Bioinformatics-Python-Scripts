import re
from random import randint

def get_shortest_super(file):
    '''reconstructs dna sequence from overlapping reads on same superstring, note: strings overlap by at least half'''
    '''file (string) name of a txt file that must be in fasta format with reads coming from the same strand of DNA'''
    
    #open the file, split superstring, remove any non ACTG from strings, remove empty strings from list
    r = [re.sub(r'[^ACTG]','', x) for x in open(file).read().split('Rosalind_') if re.search(r'[ACTG]', x)]
    #get the minimum len overlap
    init_overlap = int(len(r[0])/2)
    print(init_overlap)
    print(len(r))

    while len(r)>1:
        
        rand_int = randint(0,len(r)-1)
        x = r.pop(rand_int - 1 )
        #set a flag to see if x was put back in the list as part of a new string
        was_pushed = False
        for i in range(len(r)):
            if x[(len(x) - init_overlap):] in r[i]: 
                y = r.pop(i)
                #get the start of the shared sequence, because this sequence is from the end
                #of x, we can delete anything that comes before it in y
                index = y.find(x[len(x) - init_overlap:])
                new_string = x + y[index + init_overlap:]
                r.append(new_string)
                was_pushed = True
                break
        if not was_pushed:
            r.append(x)

    return r        

    

        
        
    
