# 1071. Greatest Common Divisor of Strings
# Sample Problem from Leetcode

# For two strings s and t, we say "t divides s" if and only if 
# s = t + ... + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x 
# such that x divides both str1 and str2.

# Johnathan Wells

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for x in reversed( range(len(str2)) ):
            found_gcd = True
            if( str2[0:x] == str1[0:x] ) :
                if( ( len(str1) % len(str2[0:x]) ) == 0 ):
                    for val in range( len(str1) / len(str2[0:x]) ) :
                        if( str1[ val*len(str2[0:x]) : (val+1)*len(str2[0:x]) ] != str2[0:x]):
                            found_gcd = False
                else:
                    found_gcd = False
            else:
                found_gcd = False
            
            if(found_gcd):
                return str2[0:x]
        return ''
    
string1 = "abcabc"
string2 = "abc"
for x in reversed( range(len(string2)+1) ):
    print(x)
    found_gcd = True
    if( string2[0:x] == string1[0:x] ) :
        if( ( len(string1) % len(string2[0:x]) ) == 0 ):
            for val in range( int(len(string1) / len(string2[0:x])) ) :
                if( string1[ val*len(string2[0:x]) : (val+1)*len(string2[0:x]) ] != string2[0:x]):
                    found_gcd = False
        else:
            found_gcd = False
    else:
        found_gcd = False
            
    if(found_gcd):
                return string2[0:x]
return ''