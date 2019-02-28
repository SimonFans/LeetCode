Let's assume number=534976, your answer should be 536479.

思路：   
先将number转成list [5,3,4,9,7,6]
从右向左找出第一个前一个数小于后面的数A
然后记录位置（i）
从i后面的部分找出大于A的最小数B
交换A和B
之后将i后的部分从小到大排序
最后得到的list写个循环变回整数

class solution():
    def nextGreaterNumber(self,input):

        number = [int(x) for x in str(input)]
        n=len(number)
        
        for i in range(n-1,0,-1):
            if number[i] > number[i-1]:
                break
        if i==0:
            return "There's no number that greater than the current one"
        # number[i-1] is the first number smaller than the right one
        num_left_end=number[i-1]
        # first regard number[i] as the smallest number
        smallest=i
        # iterate the right part list, find the smallest number in the right list, swap with the number[i-1]
        for k in range(i+1,n):
            if number[k]>num_left_end and number[k]<number[i]:
                smallest=k
        number[i-1],number[k]=number[k],number[i-1]

        # sort right list from small to large
        num_right_part=sorted(number[i:])
        # combine left list and right list
        res=number[:i]+num_right_part

        result=0
        for j in range(n):
            result=result*10+res[j]
        return result

print(solution().nextGreaterNumber(534976))
