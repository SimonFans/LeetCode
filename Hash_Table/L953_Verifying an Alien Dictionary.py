In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.


Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.


Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # how many words to compare
        N=len(words)
        # dictionary notes word position in order
        dic={c:i for i,c in enumerate(order)}
        # iterate the word list
        for i in range(N-1):
            pre,after=words[i],words[i+1]
            if pre==after:
                continue
            _len=min(len(pre),len(after))
            for j in range(_len):
                if dic[pre[j]]<dic[after[j]]:
                    break
                elif dic[pre[j]]>dic[after[j]]:
                    return False
            # case  words = ["apple","app"]
            if len(pre) > len(after) and pre[:_len]==after:
                return False
        return True
        
        
