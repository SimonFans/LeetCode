Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        
        # count unique characters in t 
        t_dict = {}
        for k in t:
            t_dict[k] = t_dict.get(k,0) + 1
        
        # count unique characters in the current window 
        window_count = {}
        
        # It should match both characters and counts in s and t
        formed = 0
        # number of unique characters in t
        required = len(set(t))
        
        # Result
        ans = (float("inf"), None, None)
        
        # left & right pointer, all starts from 0 
        l, r = 0, 0
        
        # right pointer starts to move to the right
        while r < len(s):
            character = s[r]
            window_count[character] = window_count.get(character,0) + 1
            
            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1
            if character in t_dict and window_count[character] == t_dict[character]:
                formed += 1
            # try to narrow down the window size and make it desirable
            while l <= r and formed == required:
                character = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window_count[character] -= 1
                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                if character in t_dict and window_count[character] < t_dict[character]:
                    formed -= 1
                l += 1
            r += 1   
        
        return '' if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
                
                
                
                
                
                
                
