In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. Those answers are placed in an array.

Return the minimum number of rabbits that could be in the forest.

Examples:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0
Note:

answers will have length at most 1000.
Each answers[i] will be an integer in the range [0, 999].


"""
思路：

用hashmap

dict[num] = n ,统计有n个说 num个别的兔子和自己颜色相同，如果n <= num+1,则这n个兔子颜色 相同，

即每num+1 数量组可以看成一个颜色（1组），计算n可以分成几组

如 answers = [10, 10, 10]

3只兔子说还有10个别的兔子和自己颜色一样-》dic[10] = 3

有11个兔子可以看成一个颜色比如黄色，3<11 可以看成同一组的颜色，所以至少有1组黄色的兔子-》11只

如果dic[10] = 13 > 11,那么11只是一组比如黄色，还有2只是另外一个11人组 比如红色，那么至少2组 -》22只 = 2*11


"""

import collections
import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        if len(answers)==0:
               return res
        dic=collections.defaultdict(int)
        res=0
        for answer in answers:
            dic[answer]+=1
        for key, value in dic.items():
            res+=math.ceil(value/(key+1))*(key+1)
        return res
        
