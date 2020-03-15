from itertools import groupby
def longestAlternating(S):
    temp, ans = 0, 0
    for c, g in groupby(S):
        L = len(list(g))
        ans = max(ans, temp + min(L, 2))
        temp = temp + L if L < 3 else 2
    return ans
    
S = 'baaabbabbb'
print(longestAlternating(S))

S = 'babba'
print(longestAlternating(S))

S = 'abaaaa'
print(longestAlternating(S))
