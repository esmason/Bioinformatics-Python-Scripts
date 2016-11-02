import re

def find_errors(file_name):
    ''' file_name is .txt file in FASTA format a read is considered 'correct' if it occurs twice or more, specific errors must occur at most once,'''
    file = open(file_name, 'r')
    answers = []
    correctSeq ={}
    incorrectSeq = []
    for line in file:
        if line[0] == '>':
            continue
        line = re.sub('\n', '', line)
        if line in correctSeq:
            correctSeq[line] +=1
        elif revComp(line) in correctSeq:
            correctSeq[revComp(line)] +=1
        else:
            correctSeq[line] = 1
    correct_list = [ i for i in correctSeq.items()]
    for entry in correct_list:
        if entry[1] ==1:
            del correctSeq[entry[0]]
            incorrectSeq.append(entry[0])

    for seq_wrong in incorrectSeq:
        for seq_right in correctSeq.items():
            if hamming_one(seq_wrong, seq_right[0]):
                answers.append(seq_wrong +'->'+ seq_right[0])
                break
            elif hamming_one(seq_wrong, revComp(seq_right[0])):
                answers.append(seq_wrong + '->' + revComp(seq_right[0]))
                break
    for i in answers:
        print(i)

            
        


def revComp(dna):
    compDict = dict(zip("ATCG", "TAGC"))
    ans =''
    for b in reversed(dna):
        ans += (compDict[b])
    return ans

def hamming_one(str1, str2):
    hamming = 0
    for i in range(len(str1)):
        if not str1[i] == str2[i]:
            if hamming ==1:
                return False
            else:
                assert hamming == 0
                hamming =1

    try:
        assert hamming == 1
    except AssertionError:
        raise ValueError("Hamming =" +str(hamming) + "strings: " + str1 +' ' +str2)
    return True
