Given [1,2,3]
Result:  [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

class solution(object):
    def generate_subset(self,nums):
        def dfs(nums,index,res,path):
            res.append(path)
            for i in range(index,len(nums)):
                dfs(nums,i+1,res,path+[nums[i]])
        res=[]
        dfs(nums,0,res,[])
                
        return res

print(solution().generate_subset([1,2,3]))
