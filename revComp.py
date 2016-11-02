#function returns the reverse complement of a seq
def revComp(file):
    import re

    folder = open(file, 'r')

    dna = folder.read()
    dna = re.sub(r'\n', '', dna)

    revComp = ''

    for char in dna:
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
