You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.


Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
  
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        # because you only have 2 baskets
        if n < 3:
            return n
        # sliding window left and right pointer
        left, right = 0, 0 
        # hashmap in the slding window {char:index}
        hashmap = defaultdict(int)
        # result to return 
        max_len = 2
        
        while right < n:
            hashmap[fruits[right]] = right
            if len(hashmap) == 3:
                # 找到hashmap里index最小的
                del_index = min(hashmap.values())
                del hashmap[fruits[del_index]]
                left = del_index + 1
                
            max_len = max(max_len, right-left+1)
            right+=1
        return max_len
      
