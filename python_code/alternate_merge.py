# 1768. Merge Strings Alternately
# Sample Problem from Leetcode

# You are given two strings word1 and word2. Merge the strings
# by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional 
# letters onto the end of the merged string.

# Johnathan Wells

class Solution:
    def mergeAlternately( self, word1: str, word2: str ) -> str:
        final_word = "";
        if len( word1 ) == 0:
            return word2
        elif len( word2 ) == 0:
            return word1
        else:
            if ( len ( word1 ) > len ( word2 ) ):
                for key, val in enumerate( word2 ):
                    final_word += word1[ key : key+1 : ]
                    final_word += val
                final_word += word1[ len ( word2 ) :: ]
            elif ( len ( word1 ) < len ( word2 ) ):
                for key, val in enumerate( word1 ):
                    final_word += val
                    final_word += word2[ key : key+1 : ]

                final_word += word2[ len ( word1 ) :: ]
            else:
                for key, val in enumerate( word1 ):
                    final_word += val
                    final_word += word2[ key : key+1 : ]
        return final_word