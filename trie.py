import sys
import re

"""creates and prints the edges of a trie of strings https://en.wikipedia.org/wiki/Trie from a list of DNA
sequences. the representation of each edge in the trie is as follows:
origin-node  end-node edge_letter"""
        
def read_parse_file(filename):
    f = open(filename)
    strings = []
    for line in f:
        line = re.sub('\n', '', line)
        strings.append(line)
    return strings

def create_trie(strings, branchpoint, last_node_used):
    if len(strings) == 0:
        return []
    else:
	letter = strings[0][0]
        same_first_letter = []
	for counter in range(len(strings)):
            if strings[0][0] == letter:
		s = strings.pop(0)[1:]
                if len(s) > 0:
		    same_first_letter.append(s)
	    else:
	        break
	current_node = last_node_used + 1
	left_child = create_trie(same_first_letter, current_node, current_node)
	left_last_node_used = current_node if len(left_child) == 0 else left_child[-1][1]
	right_child = create_trie(strings, branchpoint, left_last_node_used)
	this_edge = [ [branchpoint, current_node, letter] ] 
	return  this_edge + left_child + right_child
			
		

filename = re.sub("\n", "", sys.stdin.readline() )
strings = read_parse_file(filename)
sorted_strings = [s for s in sorted(strings)]
trie = create_trie(sorted_strings, 1, 1)
for elt in trie:
    elt = [str(i) for i in elt]
    print(" ".join(elt))
