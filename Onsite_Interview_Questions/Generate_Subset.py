Given [1,2,3]
Result:  [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

class solution(object):
    def generate_subset(self,nums):
        res=[]
        self.dfs(nums,0,res,[])
        return res

    def dfs(self,nums,index,res,path):
        res.append(path)
        for i in range(index,len(nums)):
            self.dfs(nums,i+1,res,path+[nums[i]])

print(solution().generate_subset([1,2,3]))
