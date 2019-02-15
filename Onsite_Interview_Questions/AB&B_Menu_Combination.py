# find menu combination, target=6.20
['Burger: 5.85', 'Fruit: 3.15', 'Fries: 3.05','drink:2.00']

Answer:
[['drink', 'Fries'], ['drink', 'Fruit'], ['Fries', 'Fruit']]

class solution(object):
    def generate_subset(self,nums):
        res=[]
        self.dfs(nums,0,res,[])
        return res

    def dfs(self,nums,index,res,path):
        res.append(path)
        for i in range(index,len(nums)):
            self.dfs(nums,i+1,res,path+[nums[i]])

menu_list=['Burger: 5.85', 'Fruit: 3.15', 'Fries: 3.05', 'drink:2.00']
menu_dic=dict()
input_price=[]
target=6.20
temp=[]
result=[]
for item in menu_list:
    menu_dic[float(item.split(':')[1])]= item.split(':')[0]
    input_price.append(float(item.split(':')[1]))
input_price.sort()
print(menu_dic)
print(input_price)
t1=solution().generate_subset(input_price)
print(t1)
for j in t1:
    if len(j)>=2 and target-sum(j)>=0:
        temp=[]
        for k in j:
            temp.append(menu_dic[k])
        result.append(temp)

print(result)

