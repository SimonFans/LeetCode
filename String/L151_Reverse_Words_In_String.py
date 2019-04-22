Given an input string, reverse the string word by word.

Example:  

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space.

class Solution:
    def reverseWords(self, s: str) -> str:
        result=''
        
        # remove trailing and split by one or more multiple spaces
        # [the,sky,is,blue]
        str_list=s.strip().split()
        
        if str_list==[]:
            return ''
        
        for i in range(1,len(str_list)):
            result+=str_list[len(str_list)-i]+' '
        
        result+=str_list[0]
        
        return result
