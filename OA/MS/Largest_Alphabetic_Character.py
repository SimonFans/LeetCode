"""
Given a string S, find the largest alphabetic character, whose both uppercase and lowercase appear in S. 
The uppercase character should be returned. For example, for S = "admeDCAB", return "D". 
If there is no such character, return "NO".
"""


s="admeDCAB"


def solution(s):
    ans='No'
    h={}
    s=set(s)
    
    for letter in s:
        val=ord(letter)
        upper=letter.upper()
        if letter not in h:
            # if letter is a uppercase a:A
            if val<96:
                h[chr(val+32)]=letter
            # if letter is a lowercase A:a
            else:
                h[chr(val-32)]=letter
        else:
            if ans == 'No':
                ans=letter.upper()
            elif ord(upper)>ord(ans):
                ans=upper
    return ans

print(solution(s))
