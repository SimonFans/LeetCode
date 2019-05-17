Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"

Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.



class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest = sorted([str(v) for v in nums], key=compare)  # 排序
        
        largest = ''.join(largest)  # 转换字符串

        return '0' if largest[0] == '0' else largest
    
class compare(str):
    def __lt__(x, y):
        return x+y > y+x
