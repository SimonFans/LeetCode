Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        i = 0
        while i < len(words):
            size = 0
            begin = i
            while i < len(words):
                newsize = len(words[i]) if size == 0 else size + len(words[i]) + 1
                if newsize <= maxWidth: 
                    size = newsize
                    i += 1
                else:
                    break
            spaceCount = maxWidth - size
            
            # check gap i-1-begin, everyCount= for each gap fill how many, spaceCount= 还多出几个
            if i - 1 - begin > 0 and i < len(words):
                everyCount = spaceCount / (i - 1 - begin)
                spaceCount %= (i - 1 - begin)
            else:
                everyCount = 0
            j = begin
            s = ''
            while j < i:
                if j > begin:
                    s += ' ' * (int(everyCount) + 1)
                    if spaceCount > 0 and i < len(words):
                        s += ' '
                        spaceCount -= 1
                s += words[j]
                j += 1
            s += ' ' * spaceCount
            ans.append(s)
        return ans      



