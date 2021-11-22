There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""
idea:
     left_part          |        right_part
A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]


"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m,n = len(nums1),len(nums2)
        # 将长度小的作为nums1,对它实施二分法查找
        if m>n:
            nums1,nums2,m,n =nums2,nums1,n,m
        # imin: short array start points
        # imax: short array length
        # half_len: 
        imin,imax,half_len=0,m,(m+n+1)//2
        while imin<=imax:
            # i: the total # of short array left cut 
            i=(imax-imin)//2+imin
            # j: the total # of long array left cut
            j=half_len-i
            # i is too small, must increase it
            if i<m and nums2[j-1]>nums1[i]:
                imin=i+1
            # 现在说名 i 太大，应该减小
            elif i>0 and nums1[i-1]>nums2[j]:
                imax=i-1
            else:
                # i 的值已经确定，现在找中间值
                # 确定左边界情况
                if i==0: max_left=nums2[j-1]
                elif j==0: max_left=nums1[i-1]
                else: max_left=max(nums1[i-1],nums2[j-1])
                # 奇数的情况下    
                if (m+n)%2==1:
                    return max_left
                # 确定右边界情况
                if i==m: min_right=nums2[j]
                elif j==n: min_right=nums1[i]
                else: min_right=min(nums2[j],nums1[i])
            
                return (max_left+min_right)/2.0
  

# Solution log(n) binary search

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        
        if  n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        k = (n1 + n2 + 1) // 2
        
        l, r = 0, n1
        
        while l < r:
            m1 = l + (r-l)//2
            m2 = k - m1
            if nums1[m1] < nums2[m2-1]:
                l = m1 + 1
            else:
                r = m1
        
        m1 = l
        m2 = k - l
        
        c1= max(float('-Inf') if m1 <= 0 else nums1[m1-1], float('-Inf') if m2 <= 0 else nums2[m2-1])
        
        if (n1+n2)%2 == 1:
            return c1
        
        c2= min(float('Inf') if m1 >= n1 else nums1[m1], float('Inf') if m2 >= n2 else nums2[m2])
        
        return (c1 + c2) /2 





        
