'''
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, 
return the shortest distance between these two words in the list.

'''

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
  
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
  
1 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2

from collections import defaultdict
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        location = defaultdict(list)
        for i, w in enumerate(wordsDict):
            location[w].append(i)
        # location: defaultdict(<class 'list'>, {'practice': [0], 'makes': [1, 4], 'perfect': [2], 'coding': [3]})
        # return searched words index list
        word1_loc = location[word1]
        word2_loc = location[word2]
        min_dist = len(wordsDict) - 1
        p1, p2 = 0, 0
        while p1 < len(word1_loc) and p2 < len(word2_loc):
            min_dist = min(min_dist, abs(word1_loc[p1]- word2_loc[p2]))
            if word1_loc[p1] < word2_loc[p2]:
                p1 += 1
            else:
                p2 += 1
        return min_dist
      
