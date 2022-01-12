You are given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
  
Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.
  
Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.
  
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        left = 0
        n = len(arr)
        _sum = 0
        # final return result
        ans = float('Inf')
        # min_len array: min length of a valid subarray ends or before i
        min_len_arr = ['Inf'] * n  
        # current minimum length
        min_len = float('Inf')
        
        for right in range(n):
            _sum += arr[right]
            while _sum > target:
                _sum -= arr[left]
                left += 1
            if _sum == target:
                cur_len = right - left + 1
                # valid answer was found before then update the potential answer
                if left > 0 and min_len_arr[left-1] != 'Inf':
                    ans = min(ans, min_len_arr[left-1] + cur_len)
                # update the minimum valid length ends at current
                min_len = min(min_len, cur_len)
                        
            min_len_arr[right] = min_len
            
        return ans if ans < float('Inf') else -1
      
      
      
