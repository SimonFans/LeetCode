Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        La=len(A)
        Lb=len(B)
        C=''
        for i in range(Lb//La+3):
            if B not in C:
                C+=A
            else:
                return i
        return -1
        
 技巧：
 尝试最多三次，如果还没有，就算找不到. 第一次如果直接找到，返回0. 否则需要初始化一个新的字符串，往里加。
