Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.

Example 1:

MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:

-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.


class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 需要两个stack，一个做正常压入，一个存到目前为止的最大值
        self.stack=[]
        self.max_stack=[]

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.max_stack)==0:
            self.max_stack.append(x)
            return
        if self.max_stack[-1]>x:
            self.max_stack.append(self.max_stack[-1])
        else:
            self.max_stack.append(x)

    def pop(self) -> int:
        if len(self.stack)!=0:
            self.max_stack.pop(-1)
            return self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        if len(self.max_stack) != 0:
            return self.max_stack[-1]

    def popMax(self) -> int:
        val=self.peekMax()
        buff=[]
        while self.top()!=val:
            buff.append(self.pop())
        self.pop()
        while len(buff)!=0:
            self.push(buff.pop(-1))
        return val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

