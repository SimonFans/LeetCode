Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
  
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
  
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # string length
        n = len(s)
        
        # edge case: if s is an empty string or k==0
        if n * k == 0:
            return 0
        
        # sliding window left and right pointers
        left, right = 0, 0 
        
        # hashmap character: its mostright position
        hashmap = defaultdict(int)
        
        # return result
        max_len = 1
            
        while right < n:
            hashmap[s[right]] = right
            # window length cannot beyond k
            if len(hashmap) == k+1:
                del_index = min(hashmap.values())
                del hashmap[s[del_index]]
                left = del_index + 1
            max_len = max(max_len, right-left +1)
            right += 1
        return max_len
