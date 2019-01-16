Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                if not (len(res) and nums1[i] != nums2[j]):
                    res.append(nums1[i])
                i += 1
                j += 1
    
        return res

    
    
    # Method2:
    class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1,c2 = collections.Counter(nums1),collections.Counter(nums2)
        return [i for i in c1.keys() for j in range(min([c1[i], c2[i]]))]
    
    or 
    
        dic1,dic2 = dict(),dict()
        for num in nums1:
            dic1[num] = dic1.get(num,0) + 1
        for num in nums2:
            dic2[num] = dic2.get(num,0) + 1
        return [x for x in dic2 for j in range(min(dic1.get(x,0),dic2.get(x,0)))]

