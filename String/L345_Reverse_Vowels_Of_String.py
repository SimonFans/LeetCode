Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left,right=0,len(s)-1
        vowels=['a','e','i','o','u']
        ls=list(s)
        while left < right:
            while left<right and ls[left].lower() not in vowels:
                left+=1
            while left < right and ls[right].lower() not in vowels:
                right-=1
                
            ls[left],ls[right]=ls[right],ls[left]
            left+=1
            right-=1
        return ''.join(ls)
