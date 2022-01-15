'''
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth. Let maxDepth be the maximum depth of any integer.

The weight of an integer is maxDepth - (the depth of the integer) + 1.

Return the sum of each integer in nestedList multiplied by its weight.

'''

Input: nestedList = [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's with a weight of 1, one 2 with a weight of 2.
1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8


Input: nestedList = [1,[4,[6]]]
Output: 17
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1.
1*3 + 4*2 + 6*1 = 17


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

'''
weight = maxDepth - (the depth of the integer) + 1

'''

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # get the maximum depth
        def findmaxDepth(nestedList):
            depth = 1
            for curr in nestedList:
                if not curr.isInteger():
                    depth = max(depth, 1 + findmaxDepth(curr.getList()))
                    print(depth)
            return depth
        
        def weightSum(nestedList, depth, maxDepth):
            res = 0
            for curr in nestedList:
                if not curr.isInteger():
                    res += weightSum(curr.getList(), depth +1, maxDepth)
                else:
                    res += curr.getInteger() * (maxDepth - depth + 1)
            return res
            
        
        # depth at least is 1
        maxDepth = findmaxDepth(nestedList)
        answer = weightSum(nestedList, 1, maxDepth)
        return answer
      
      
      
      
