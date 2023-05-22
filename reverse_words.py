# 151. Reverse Words in a String
# Sample Problem from Leetcode

# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.

# Johnathan Wells

class Solution:
    def reverseWords(self, s: str) -> str:
        final_list = []
        index_init = -1
        index_final = -1
        for key, char in enumerate(s):
            if( not (char.isspace()) and (index_init == -1) ):
                index_init = key
            elif( (char.isspace()) and (index_init != -1)):
                index_final = key
                final_list.append(s[index_init:index_final])
                index_init = -1
                index_final = -1
            if( (key == len(s)-1) and (index_init != 1) ):
                final_list.append(s[index_init:len(s)])
        
        final_str = ''

        for val in reversed(final_list):
            final_str += val + ' '
        final_str = final_str.strip()

        return final_str