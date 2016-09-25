class KMP(object):
    def contains_pattern(self, string, pattern):
        string_index = 0
        pattern_index = 0
        pattern_table = build_kmp_table(pattern)
        contains = False
        while string_index < len(string):
            if string[string_index] == pattern[pattern_index]:
                pattern_index += 1
                if pattern_index == len(pattern):
                    contains = True
                    break
            else:
                pattern_index = pattern_table[pattern_index]
            string_index += 1
        return contains
            


    def build_kmp_table(self,pattern, print_table = False):
        j = 0
        i = 1
        table = [0 for l in pattern] 
        while i < len(pattern) :
            if pattern[i] == pattern[j]:
                table[i] = j  + 1
                i += 1
                j += 1
            elif j>0:
                j = table[j-1]
            else:
                table[i] = 0
                i += 1
        if print_table:
            for i in table:
               print(i, end = ' ')
            print('') 
        return table



