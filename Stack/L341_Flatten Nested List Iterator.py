Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].
             
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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
 
class NestedIterator(object):
 
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [ni for ni in reversed(nestedList)]  #反序压入栈，使第一个元素在栈顶
 
    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()  #是整数的时候pop出栈
 
    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:           #栈不为空的时候执行下面程序
            top = self.stack[-1]    # 取栈顶
            if top.isInteger():     # 当栈顶是整数的时候
                return True         #返回true，本题中就去执行next 的程序了
            top = self.stack.pop()  #如果栈顶不是整数，而是列表类型的
            for ni in reversed(top.getList()):  #又将列表里面元素反序压入栈
                self.stack.append(ni)
 
        return False
 
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

--------------------- 
作者：maymay_ 
来源：CSDN 
原文：https://blog.csdn.net/maymay_/article/details/80162847 
版权声明：本文为博主原创文章，转载请附上博文链接！
