import urllib.request
import re
folder = open('uniprot.txt', 'r')
file = folder.read()
listP = file.split('\n')
listP = listP[:len(listP)-1]
listFasta = []
for e in listP:
    response = urllib.request.urlopen('http://www.uniprot.org/uniprot/' + e +'.fasta')
    html = response.read().decode('utf8')
    listFasta.append(html)


for i in range(len(listFasta)):
    seq = listFasta[i]
    seq = re.split('\n', seq)
    seq = seq[1:]
    seq=''.join(seq)
    listFasta[i] = seq

positionslist=[]
for seq in listFasta:
    positions = []
    for i in range(len(seq)-3 ):
        if (len(re.sub(r'N(?!P)[A-Z][S|T](?!P)[A-Z]', '' , seq[i:(i+4)]))==0):
            positions.append(i+1)
    positionslist.append(positions)

results = open("protRes.txt", 'w')

for p in range(len(positionslist)):

    if len(positionslist[p])>0:
        results.write(listP[p]+ '\n')

    for i in positionslist[p]:
        results.write(str(i)+ " ")
    
    results.write("\n")

results.close()


