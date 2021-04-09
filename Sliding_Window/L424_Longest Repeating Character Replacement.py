Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Solution:
  
# Test Case: AABCABBB should return 6
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Get the string length
        str_len = len(s)
        # edge case
        if str_len < 2:
            return str_len
        # define an array to count uppercase letters
        charCount = [0]*26
        # from current point to previous
        maxCount = 0
        # used to return result
        res = 0
        # define the left & right pointer
        left, right = 0, 0
        # Iterate the string from left to right
        while right < str_len:
            charCount[ord(s[right])-ord('A')] += 1
            maxCount = max(maxCount, charCount[ord(s[right])-ord('A')])
            right += 1
            if right - left - maxCount > k:
                charCount[ord(s[left])-ord('A')] -= 1
                left += 1
            
        return right - left
      
