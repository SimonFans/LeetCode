'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
  
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        
        # Base condition
        if s1_len > s2_len:
            return False
        
        s1_c = Counter(s1)
        s2_c = defaultdict(int)
        left = 0
        
        for right, val in enumerate(s2):
            s2_c[val] += 1
            # window condition
            if right - left + 1 > s1_len:
                if s2_c[s2[left]] == 1:
                    del s2_c[s2[left]]
                else:
                    s2_c[s2[left]] -= 1
                left += 1
            if s1_c == s2_c:
                return True
        return False

