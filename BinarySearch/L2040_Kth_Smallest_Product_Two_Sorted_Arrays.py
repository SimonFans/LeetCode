'''
        2  3 i
        4  8 12
     j  5 10 15
'''
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:  
        def count(A, B, x):
            cnt = 0
            j = len(B) - 1
            for i in range(len(A)):
                while j>=0 and A[i]*B[j] > x:
                    j-=1
                cnt += j + 1
            return cnt
        
        # split into four pieces. nums1 split into 2 lists (negative, postive), nums2 split into 2 lists (negative, postive)
        # For those negative ones, inverse the value and reverse the list to make it like positive increasing list
        neg_A = [-num for num in nums1 if num < 0][::-1]
        pos_A = [num for num in nums1 if num >=0]
        neg_B = [-num for num in nums2 if num < 0][::-1]
        pos_B = [num for num in nums2 if num >=0]
        
        # Negative count, which is used to compare with k value later
        neg_cnt = len(neg_A)*len(pos_B) + len(pos_A)*len(neg_B)
        
        # if the asked smallest k > negative numbers count, then minus those negative count, 
        # search from positive range, flag positive
        if k > neg_cnt:
            k -= neg_cnt
            flag = 1
        # if the asked smallest k is less than negative numbers count, then search from remaining negaive numbers
        else:
            k = neg_cnt - k + 1
            pos_B, neg_B  = neg_B, pos_B
            flag = -1
            
        # due to the value range which is from -10^5 to 10^5
        left, right = 0, 10**10
        while left < right:
            mid = left + (right-left) // 2
            if count(neg_A, neg_B, mid) + count(pos_A, pos_B, mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left * flag
      
      
