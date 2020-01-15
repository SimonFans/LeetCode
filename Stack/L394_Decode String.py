Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


"""
curstring = prestring + prenum * curstring，prestring是前面的字符串，prenum * curstring是这一步骤结束之后的字符串，
所以是前面的字符串+现在的字符串得到目前已有的字符串。

"""

class Solution:
    def decodeString(self, s: str) -> str:
        if len(s)==0:
            return ""
        curr_string=""
        curr_num=0
        stack=[]
        for char in s:
            if char=='[':
                stack.append(curr_string)
                stack.append(curr_num)
                curr_string=""
                curr_num=0
                
            elif char==']':
                pre_num=stack.pop()
                pre_string=stack.pop()
                curr_string=pre_string+pre_num*curr_string
                
            elif char.isdigit():
                curr_num=curr_num*10+int(char)
            # only alphabet
            else:
                curr_string+=char
        return curr_string
        
   
