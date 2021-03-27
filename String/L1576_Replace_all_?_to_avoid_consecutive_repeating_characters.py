# L1576. Replace All ?'s to Avoid Consecutive Repeating Characters

'''
Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. 
Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".

Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. 
Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".

Input: s = "j?qg??b"
Output: "jaqgacb"

Input: s = "??yw?ipkj?"
Output: "acywaipkja"

'''

class Solution:
    def modifyString(self, s: str) -> str:
        # define a string variable to return
        res = ''
        # Get the given string length 
        n = len(s)
        # edge case can be when the length of string is 1
        if n == 1:
            return 'a'
        # iterate the string from left to right, write condition for ?
        # if current pos is '?' (discuss 3 cases, start, middle, end) else add the char to the res
        for i, ch in enumerate(s):
            if ch == '?':
                # ? at the start case
                if i == 0:
                    for c in 'abc':
                        if c != s[i+1]:
                            res += c
                            break
                # ? not at the start or end
                elif i < n-1:
                    for c in 'abc':
                        if c != res[-1] and c != s[i+1]:
                            res += c
                            break
                # ? at the end case
                elif i == n-1:
                    for c in 'abc':
                        if c != res[-1]:
                            res += c
                            break
            else:
                res += ch
        return res


