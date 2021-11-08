Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.



from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # return value
        max_len = 0
        # sliding window left boundary
        i = 0
        # distinct characters count 
        distinct_cnt = 0
        # char : count dictionary
        char_num = defaultdict(int)
        
        for j in range(len(s)):
            if char_num[s[j]] == 0:
                distinct_cnt += 1
            char_num[s[j]] += 1
            
            while distinct_cnt > k:
                char_num[s[i]] -= 1
                if char_num[s[i]] == 0:
                    distinct_cnt -= 1
                i += 1
            max_len = max(max_len, j - i + 1)
        return max_len        
