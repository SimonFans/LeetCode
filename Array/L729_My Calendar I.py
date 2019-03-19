Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.

Method 1:

class Node(object):
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.left = None
        self.right = None
        

class MyCalendar:

    def __init__(self):
        self.root=None
    
    # node=> root
    def book_helper(self, s,e,node):  
        if node.e<=s:
            if node.right:
                return self.book_helper(s,e,node.right)
            else:
                node.right=Node(s,e)
                return True
        elif e <= node.s:
            if node.left:
                return self.book_helper(s,e,node.left)
            else:
                node.left=Node(s,e)
                return True
        else:
            return False
            

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root=Node(start,end)
            return True
        else:
            return self.book_helper(start, end, self.root)
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

Method 2:

class MyCalendar(object):
    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for s, e in self.calendar:
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True
        
        
