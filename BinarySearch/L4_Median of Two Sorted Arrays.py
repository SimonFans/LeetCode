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


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m,n = len(nums1),len(nums2)
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
            elif i>0 and nums1[i-1]>nums2[j]:
                imax=i-1
            else:
                if i==0: max_left=nums2[j-1]
                elif j==0: max_left=nums1[i-1]
                else: max_left=max(nums1[i-1],nums2[j-1])
                if (m+n)%2==1:
                    return max_left
                if i==m: min_right=nums2[j]
                elif j==n: min_right=nums1[i]
                else: min_right=min(nums2[j],nums1[i])
            
                return (max_left+min_right)/2.0
            
