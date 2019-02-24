#1.给一个string，可能是一个单词，可能是一段话， 要求返回最长的重复的substring。例如：
#Input："I like apple, I like banana." Output: "I like"
#Input: "banana" Output: "ana"


class solution():
    def Max_Repeat_Substring(self,str):
        max=0  # 相同字符连续出现的最大长度
        k=0   # 记录了相同字符连续出现的个数
        # i： 字符间距从1开始递增
        for i in range(1,len(str)):
            for j in range(len(str)-i):
                if str[j]==str[i+j]:
                    k+=1
                else:
                    k=0
                if k>max:
                    max=k
                    first=j-k+1 #定位答案首字符出现的位置
        return str[first:first+max]


input="I like apple, I like banana."
#input= "I like apple, I like banana."
print(solution().Max_Repeat_Substring(input))
