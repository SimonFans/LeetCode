Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

Example 1:

Input: [1,0,1,0,1]
Output: 1

Explanation: 
There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.

Example 2:

Input: [0,0,0,1,0]
Output: 0

Explanation: 
Since there is only one 1 in the array, no swaps needed.

Example 3:

Input: [1,0,1,0,1,0,0,1,1,0,1]
Output: 3

Explanation: 
One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].


class Solution():
    def minSwap(self,arr):
        
        n=len(arr)
        num_ones=0
        # 计算整个array里面有多少个1
        for i in range(n):
            if arr[i]==1:
                num_ones+=1
        
        # 计算第一组长度=num_ones的窗口中有多少个1，然后用num_ones-cur_ones就是当前窗口需要交换1的次数
        temp=arr[:num_ones]
        cur_ones=temp.count(1)
        res=num_ones-cur_ones
        
        for i in range(1,n-num_ones+1):
            temp=arr[i:i+num_ones]
            cur_ones1=temp.count(1)
            print(cur_ones1)
            res=min(res,num_ones-cur_ones1)
            print("res",res)
        return res
        

#arr=[1,0,1,0,1]
#arr=[0,0,0,1,0]
arr=[1,0,1,0,1,0,0,1,1,0,1]
print(Solution().minSwap(arr))


