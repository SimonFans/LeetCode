import os
from os.path import join, getsize

class solution:

    def __init__(self):
        self.items={}
        self.temp=[]
        self.output=[]

    def getResult(self,input):
        for dirpath,dirnames,filenames in os.walk(input):
            for file in filenames:
                temp=join(str(dirpath),str(file))
                self.temp.append(temp)
        print(self.temp)    # print complete file path under a certain directory
        for item in self.temp:
            t=item.split(' ') # string to list
            if getsize(item) not in self.items:
                self.items[getsize(item)]=t
            else:
                self.items[getsize(item)].append(item)

        print(self.items)  # print <length: list format>

        for i in self.items:
            self.output.append(self.items.get(i))
        return self.output

input="/Users/simon/Desktop/test"
test=solution()
print(test.getResult(input))
