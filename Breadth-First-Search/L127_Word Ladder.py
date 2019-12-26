Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.



Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.


Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # ensure no duplicated word in the list
        wordList=set(wordList)
        # insert beginWord into the queue, mark 1 means one time
        queue=collections.deque()
        queue.append([beginWord,1])
        while queue:
            word,length=queue.popleft()
            # when the word is same as endWord, return length
            if word==endWord:
                return length
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    w=word[:i]+c+word[i+1:]
                    if w in wordList:
                        wordList.remove(w)
                        queue.append([w,length+1])
        return 0
    
