Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
  
Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.
  
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def removeNestings(nested_list, depth):
            res = 0
            for curr in nested_list:
                # curr is a nested list
                if not curr.isInteger():
                    res += removeNestings(curr.getList(), depth+1)
                # curr is an integer
                else:
                    res += curr.getInteger() * depth
            return res
        
        depth = 1
        return removeNestings(nestedList, depth)

# 如果没有给class

import collections
class Solution:
    def depthSum(self, nestedList) -> int:
        def removeNestings(l, depth):
            res = 0
            for curr in l:
                if type(curr)==list:
                    res += removeNestings(curr, depth+1)
                else:
                    res += curr * depth
            return res
        
        depth =1
        return removeNestings(nestedList, depth)
    
    
    
    
    
    
    
    
