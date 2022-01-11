You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.


Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.


Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
  
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
  
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Get string length & number of words
        n, num_words = len(s), len(words)
        # base edge case
        if n == 0 or num_words == 0:
            return []
        # count how many per each word in words {bar:1, foo:1}
        count = collections.Counter(words)
        # Get length of word length
        word_len = len(words[0])
        # Total concatenation word length
        total_len = num_words * word_len
        
        res = []
        
        left = 0
        
        while left <= n - total_len:
            # determine whether s[i:i+total_len] is valid
            seen = collections.defaultdict(int)
            
            for j in range(left, left + total_len, word_len):
                w = s[j:j + word_len]
                if w in count:
                    seen[w] += 1
                    if seen[w] > count[w]:
                        break
                else:
                    break
            # if words in seen == words appear in count, compare the key not value
            if seen == count:
                res.append(left)
            left = left + 1
        return res
      
