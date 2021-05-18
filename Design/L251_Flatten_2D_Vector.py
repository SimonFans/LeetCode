'''
Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.

Implement the Vector2D class:

Vector2D(int[][] vec) initializes the object with the 2D vector vec.
next() returns the next element from the 2D vector and moves the pointer one step forward. You may assume that all the calls to next are valid.
hasNext() returns true if there are still some elements in the vector, and false otherwise.


Input
["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
[[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]

Output
[null, 1, 2, 3, true, true, 4, false]

Explanation
Vector2D vector2D = new Vector2D([[1, 2], [3], [4]]);
vector2D.next();    // return 1
vector2D.next();    // return 2
vector2D.next();    // return 3
vector2D.hasNext(); // return True
vector2D.hasNext(); // return True
vector2D.next();    // return 4
vector2D.hasNext(); // return False

'''

Solution:
  
class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.inner = 0
        self.outer = 0
        self.vector = vec

    def next(self) -> int:
        self.when_to_next()
        res = self.vector[self.outer][self.inner]
        self.inner += 1
        return res

    def hasNext(self) -> bool:
        self.when_to_next()
        return self.outer < len(self.vector)
    
    # 什么时候更新outer和inner指针
    # 1. 当外部指针的index小于整个list的长度
    # 2. 当内部指针到达最大子list的长度，即外部指针的长度
    # 这个时候需要外指针后移，内部指针清0重计
    def when_to_next(self):
        while self.outer < len(self.vector) and self.inner == len(self.vector[self.outer]):
            self.outer += 1
            self.inner = 0
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()

