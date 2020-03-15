class Solution:
    def solution(self, s):
        right = Counter(s)
        left = Counter()
        ans = left['B'] + right['A']
        print(ans)
        for c in s:
            left[c] += 1
            right[c] -= 1
            ans = min(ans, left['B'] + right['A'])
        return ans
