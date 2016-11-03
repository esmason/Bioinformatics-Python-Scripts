from bioDecorators import fastaReader
import re

'''this script is a modification of editDistAlign.py that finds an optimal alignment and alignment score using
weights from a scoring matrix which preference more "biologically feasible" substutions 
https://en.wikipedia.org/wiki/Substitution_matrix#Background '''

FILENAME = "BLOSUM62.txt"
GAP_PENALTY = - 5
FASTA_SEQ_FILE = "rosalind_glob.txt"

@fastaReader
def find_alignment(fasta_list):
    string1 =fasta_list[0][1]
    string2 = fasta_list[1][1]
    #init 'soln so far' tables
    distTable = [[None for x in range(len(string2) +1)] for x in range(len(string1)+1)]
    strTable = [[None for x in range(len(string2) +1)] for x in range(len(string1)+1)]
    scoring_mtx = read_scoring_matrix(FILENAME)
    for i in range(len(string1)+1):
        for j in range(len(string2)+1):
            if i == 0 or j == 0:
                #initialize base case with gap penalty times number of gaps
                distTable[i][j] = min(GAP_PENALTY * i, GAP_PENALTY * j)
                strTable[i][j] = ('','')
            else:
		replace_letter = distTable[i-1][j-1] + scoring_mtx[string1[i-1]][string2[j-1]]
                maxscore = max(distTable[i-1][j] + GAP_PENALTY, distTable[i][j-1] + GAP_PENALTY, replace_letter)
                if replace_letter == maxscore:
                    strTable[i][j] = (strTable[i-1][j-1][0] + string1[i-1] , strTable[i-1][j-1][1] + string2[j-1])
                elif distTable[i][j-1]  + GAP_PENALTY== maxscore:
                    strTable[i][j] = (strTable[i][j-1][0]+ '-', strTable[i][j-1][1] + string2[j-1])

                elif distTable[i-1][j] + GAP_PENALTY == maxscore:
                    strTable[i][j] = (strTable[i-1][j][0] + string1[i-1], strTable[i-1][j][1] + '-')
                distTable[i][j] = maxscore 
    distance = distTable[len(string1)][len(string2)]
    alignment = [ strTable[len(string1)][len(string2)][0],
              strTable[len(string1)][len(string2)][1]  ]
    return(distance, alignment)

def read_scoring_matrix(filename):
	'''Reads a text file of a scoring matrix such as BLOSUM62.txt and converts it to a dictionary of dictionaries
	   representation of the matrix st the outer dict is rows/columns and inner dict is rows/columns (as scoring
	   matrix S is symmetric S.T == S) '''
	mat_file = open(filename)
	amino_acids_list = [re.sub('\n', '',aa) for aa in mat_file.readline().split(' ') if not aa == '']
	amino_acids_dict = dict([(aa,None) for aa in amino_acids_list])
	for i in range(len(amino_acids_dict.keys())):
		row =	[re.sub('\n', '', elt) for elt in mat_file.readline().split(' ') if not elt == '']
		#pop the letter of each row off
		letter = row.pop(0)
		row_dict = dict(zip(amino_acids_list, [int(num) for num in row]))
		amino_acids_dict[letter] = row_dict
	return amino_acids_dict

print(find_alignment(FASTA_SEQ_FILE))
