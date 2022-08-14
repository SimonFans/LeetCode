Onsite
第一轮coding，一小时。设计类似HashMap的功能，支持get, set, delete和undo和redo操作， 允许直接调用hashmap， 主要考的是undo 和 redo 的实现。（我用了stack)

第二轮是coding，一个半小时。给一个单链表，每一个node都含有一个word。另外给一段长的text，问能不能在这个单链表中顺序找到给定的这个text。注意 edge case
input:  
LinkedList: face -> mask - > is -> good
Target string: isgood 
output: true

第三轮系统设计，一个小时，设计 get 和 update database的接口。 table 有messageBody 和messageId。 面试官问了很多问题，比如 h‍‌‌‍‌‌‍‌‌‍‍‌‌‌‍‌‌‌‌ttp status code 和handle exception ， retry policy， 如何控制多个client 想更新同一个数据等等。个人感受: 和这个engineer聊天，我感受到了他们内部的系统写的好像不是很好，。。。 可能是我想多了。。。我觉得和这个人一起干活， 一定很吃力。。。

第四轮是manager面， 常规bq问题

总结， 把面经背熟，然后去面试吧。。。 接下来的面试者，加油了！ 


class MyHashMap:

    def __init__(self):
        self.hashMap = {}
        self.undo_stack = []
        self.redo_stack = []

    def put(self, key, value):
        self.hashMap[key] = value
        self.undo_stack.append((key,value))

    def get(self, key):
        if key in self.hashMap:
            return self.hashMap[key]
        return -1

    def remove(self, key):
        if key in self.hashMap:
            for k,v in self.undo_stack:
                if k == key:
                    self.undo_stack.remove((k,v))
                    self.redo_stack.append((k,v))
                    break
            del self.hashMap[key]
            
    def undo(self):
        if not self.undo_stack:
            return -1
        k, v = self.undo_stack.pop()
        self.hashMap.pop(k)
        self.redo_stack.append((k,v))
        
    def redo(self):
        if not self.redo_stack:
            return -1
        k, v = self.redo_stack.pop()
        self.put(k,v)
        
obj = MyHashMap()
obj.put(1,1)
obj.put(2,2)
obj.put(3,3)
obj.put(4,4)
print('hashmap:', obj.hashMap)
print('undo', obj.undo_stack)
print('redo:', obj.redo_stack)
obj.undo()
print('hashmap:', obj.hashMap)
print('undo', obj.undo_stack)
print('redo:', obj.redo_stack)
obj.redo()
print('hashmap:', obj.hashMap)
print('undo', obj.undo_stack)
print('redo:', obj.redo_stack)
print('removing.....')
obj.remove(2)
print('hashmap:', obj.hashMap)
print('undo', obj.undo_stack)
print('redo:', obj.redo_stack)
print('redo...')
obj.redo()
print('hashmap:', obj.hashMap)face
print('undo', obj.undo_stack)
print('redo:', obj.redo_stack)
