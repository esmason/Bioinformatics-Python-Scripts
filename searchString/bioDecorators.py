'''  function wrappers for bioinformatics
    fastaReader - Parse .txt files containing fasta format data
    TODO
      -download fasta format data  '''
      

#import urllib2


def fastaReader(func):
    def inner(filename, *args):
        '''this is a wrapped function the filename containing the FASTA files must be the first positional arg'''

        with open(filename) as file:
            fasta_list = []

            #creates a list of lists of strings, s.t. [(fasta_id1, sequence1),....]
            for line in file:
                if line[0] == '>':
                    fasta_list.append( [line.lstrip('>').rstrip('\n'), '' ] )
                else:
                    fasta_list[-1][1] += line.rstrip('\n')
                                                           
        return func(fasta_list)

    return inner

def fastaURL(func):
    #TODO
    pass
    
