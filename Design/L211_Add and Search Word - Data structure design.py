Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_dict=collections.defaultdict(list)
        

    def addWord(self, word: 'str') -> 'None':
        """
        Adds a word into the data structure.
        """
        if word:
            self.word_dict[len(word)].append(word)
        

    def search(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for dic_word in self.word_dict[len(word)]:
            for i, ch in enumerate(word):
                if ch!=dic_word[i] and ch!='.':
                    break
            else:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

