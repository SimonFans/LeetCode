
Question:
Flatten array: [1,2,3,[4,5,[6]]] -> [1,2,3,4,5,6] 


class solution:
    output=[]
    def removNestings(self,l):
        for i in l:
            if type(i)==list:
                self.removNestings(i)
            else:
                self.output.append(i)
        return self.output

t=[1,2,3,[4,5,[6]]]
test=solution()
print(test.removNestings(t))
