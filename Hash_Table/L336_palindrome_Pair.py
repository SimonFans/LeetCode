'''
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Input: words = ["a",""]
Output: [[0,1],[1,0]]
'''

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def all_valid_suffix(word):
            valid_suffix = []
            for i in range(len(word)):
                if word[:i+1] == word[:i+1][::-1]:
                    valid_suffix.append(word[i+1:])
            return valid_suffix
        
        def all_valid_prefix(word):
            valid_prefix = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    valid_prefix.append(word[:i])
            return valid_prefix
        
        word_lookup = {word:i for i, word in enumerate(words)}
        ans = []
        
        # case1: 
        # Reverse each string and see if there's any same in the word lookup
        # Add to the final solution if their index is different
        for word_index, word in enumerate(words):
            reverse_str = word[::-1] 
            # index different to prevent single char like 's', you got result [3,3]
            if reverse_str in word_lookup and word_index != word_lookup[reverse_str]:
                ans.append([word_index, word_lookup[reverse_str]])
        
        # case2: valid suffix
        # example: abc => bc will be into the valid suffix
        # example: aabc => abc and bc will be into the valid suffix
        # note: case => ['a',''] case2 & 3 last append switch position, res will include [0,1] and [1,0] otherwise it's [0,1] and [0,1]
            for suffix in all_valid_suffix(word):
                reverse_suffix = suffix[::-1]
                if reverse_suffix in word_lookup:
                    ans.append([word_lookup[reverse_suffix], word_index])
        
        # case3: valid prefix
        # example: abc => ab will be into the valid prefix
        # example: aabc => aab will be into the valid suffix
            for prefix in all_valid_prefix(word):
                reverse_prefix = prefix[::-1]
                if reverse_prefix in word_lookup:
                    ans.append([word_index, word_lookup[reverse_prefix]])
        return ans    
        
