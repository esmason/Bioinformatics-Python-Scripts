#translates an RNA sequence (incl any stop codons) into AA seq
def translate(file):
    folder = open(file, 'r')
    rna =  folder.read()
    for char in rna:
        if ((char == '\n') or (char == 'n')):
            print('here')
            rna.replace(char, '')
    rna = rna[0:(len(rna) -1)]
    bases = ['U', 'C', 'A', 'G']
    codons = [a+b+c for a in bases for b in bases for c in bases]
    proteins = ['F', 'F', 'L', 'L', 'S', 'S','S','S', 'Y', 'Y', 'Stop', 'Stop', 'C',
                'C', 'Stop', 'W', 'L', 'L', 'L','L', 'P','P','P','P','H','H','Q','Q',
                'R','R','R','R','I','I','I', 'M','T','T','T','T','N', 'N', 'K', 'K','S','S','R',
                'R','V','V','V','V','A','A','A','A','D','D','E','E', 'G', 'G', 'G', 'G']
    codonDict = dict(zip(codons, proteins))
    proteinStr = ''
    for i in range(0, len(rna), 3):
        proteinStr = proteinStr + codonDict[rna[i:(i+3)]]
    return proteinStr
