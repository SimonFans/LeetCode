from collections import Counter
def minStepEqualPiles(A):
    cnt = Counter(A)
    nums = sorted(cnt.keys(), reverse=True)
    k, ans = 0, 0
    for x in nums[:-1]:
        k += cnt[x]
        ans += k
    return ans

A = [5, 2, 1]
print(minStepEqualPiles(A))

A = [4, 5, 5, 4, 2]
print(minStepEqualPiles(A))
