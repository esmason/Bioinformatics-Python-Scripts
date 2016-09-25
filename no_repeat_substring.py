""" 
computes length of longest substring of s
with no repeats in O(n) time

eg. for "abcabcda" return 4 for "abcd" or "bcda" 
"""

def length_of_longest_substring(self, s):
    letter_dict = dict()
    current_start = 0
    current_end = 0
    max_length = 0
    for i in range(len(s)):
        current_end = i
        try:
            last_pos = letter_dict[s[i]]
            if last_pos >= current_start:
                current_start = last_pos + 1
        except KeyError:
            pass
        letter_dict[s[i]] = i
        max_length = max((current_end - current_start + 1), max_length)
    return max_length
