'''
Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

Implement the WordDistance class:

WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.
'''

Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]

Explanation
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // return 3
wordDistance.shortest("makes", "coding");    // return 1


# 两个单词的距离： 两个单词的index差的绝对值

from collections import defaultdict

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.location = defaultdict(list)
        # Hashmap: stores key, value pair. key is the word, and value is the index
        # the index is already sorted with for loop
        for i, w in enumerate(wordsDict):
            self.location[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        # Get the searched word index list from the predefined dictionary
        loc1 = self.location[word1]
        loc2 = self.location[word2]
        # two pointers to point on each index list
        p1, p2 = 0,0 
        short_dist = float('Inf')
        print(loc1)
        print(loc2)
        while p1 < len(loc1) and p2 < len(loc2):
            short_dist = min(short_dist, abs(loc1[p1]-loc2[p2]))
            if loc1[p1] < loc2[p2]:
                p1 += 1
            else:
                p2 += 1
        return short_dist
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

