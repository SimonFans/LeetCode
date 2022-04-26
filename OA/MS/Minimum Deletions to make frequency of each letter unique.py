class Solution:
    def minDeletions(self, s: str) -> int:
        frequency = [0] * 26
        for char in s:
            frequency[ord(char) - ord('a')] += 1
        delete_count = 0
        seen_frequency = set()
        for i in range(26):
            while frequency[i] and frequency[i] in seen_frequency:
                frequency[i] -= 1
                delete_count += 1
            seen_frequency.add(frequency[i])
        return delete_count

print(minDeletion("eeeeffff"))
print(minDeletion("aabbffddeaee"))
print(minDeletion("llll"))
print(minDeletion("example"))
