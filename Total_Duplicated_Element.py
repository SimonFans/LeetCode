class solution():

    count=0

    def find_total_duplicate(self,A):
        dict={}
        for i in A:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        print(dict)
        for key in dict:

            if dict.get(key) >1:
                self.count+=1
        return self.count

A=[10,20,10,10,30,20]
test=solution()
print(test.find_total_duplicate(A))