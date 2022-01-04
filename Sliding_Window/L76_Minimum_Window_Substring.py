'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not s or not t or len(s) < len(t):
            return ''
        
        left, right = 0, 0
        # target dictionary
        target_dict = Counter(t)
        # number of unique characters in t
        required = len(target_dict)
        
        # if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        expect = 0
        
        window_count = collections.defaultdict(int)
        
        # initial the max len is len(s)+1. why +1 is because if s = 'a', t ='a', line 28 will be wrong
        ans = ' '*(len(s)+1)
        
        while right < len(s):
            window_count[s[right]] += 1
            # compare #(current chars) == #(chars in t), if so expect+=1
            if s[right] in target_dict and window_count[s[right]] == target_dict[s[right]]:
                expect += 1
            # update miniLen, while loop ends when left > right or expect < required
            while left <= right and expect == required:
                if right -left + 1 < len(ans):
                    ans = s[left:right+1]
                window_count[s[left]] -= 1
                if s[left] in target_dict and window_count[s[left]] < target_dict[s[left]]:
                    expect -= 1
                left += 1
            right +=1
        return '' if len(ans) == len(s)+1 else ans
      
