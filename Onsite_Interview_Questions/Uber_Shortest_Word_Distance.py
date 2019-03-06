Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


# O(n+m) better than O(n)
class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.dic = {}
        self.l = len(words)
        for index, value in enumerate(words):
            self.dic[value] = self.dic.get(value, []) + [index] 

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = self.dic[word1], self.dic[word2]
        i = j = 0
        res = self.l
        # O(m+n) time complexity
        while i < len(l1) and j < len(l2):
            res = min(res, abs(l1[i]-l2[j])) # loop all the l1 and l2 to find the shortest
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return res
