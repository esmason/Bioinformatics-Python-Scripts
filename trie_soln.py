import re
import sys
from os import path
from Trie import Trie


def read_console():
    filename = re.sub("\n", "", sys.stdin.readline() )
    if path.isfile(filename):
        return filename
    else:
        print("that file does not exist please try again")
        return read_console()

def trie_soln():
    trie_methods = Trie()
    print("please enter filename")
    filename = read_console()
    strings = trie_methods.read_parse_file(filename)
    trie = trie_methods.create_trie(strings, 1, 1)
    for elt in trie:
        elt = [str(i) for i in elt]
        print(" ".join(elt))

trie_soln()
