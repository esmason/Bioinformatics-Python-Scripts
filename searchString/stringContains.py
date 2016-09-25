from bioDecorators import fastaReader

from kmp import KMP

@fastaReader
def kmp_array(fasta_list):
    kmp = KMP()
   
    kmp.build_kmp_table(fasta_list[0][1], print_table = True)

kmp_array('rosalind_kmp.txt')
    
