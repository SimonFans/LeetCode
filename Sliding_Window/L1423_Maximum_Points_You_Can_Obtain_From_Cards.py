# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

# Your score is the sum of the points of the cards you have taken.

# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. 
The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
  
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
  
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # choose cards from the beginning or end of the array in such a way that the sum of the remaining cards is minimized.
        total_score = sum(cardPoints)
        n = len(cardPoints)
        if n == k:
            return total_score
        # first give the maximum value to minSubarrayScore
        minSubarrayScore = total_score
        presentSubarrayScore = 0
        requiredSubarrayLength = n - k 
        left = 0
        
        for right in range(n):
            presentSubarrayScore += cardPoints[right]
            if right - left + 1 == requiredSubarrayLength:
                minSubarrayScore = min(minSubarrayScore, presentSubarrayScore)
                presentSubarrayScore -= cardPoints[left]
                left += 1
        return total_score - minSubarrayScore
      
      
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        front_score, rear_score = 0, 0
        n = len(cardPoints)
        for i in range(k):
            front_score +=  cardPoints[i]
        # assume the current sum is the maximum
        max_score = front_score
        
        for i in range(k-1,-1,-1):
            rear_score += cardPoints[n-k+i]
            front_score -= cardPoints[i]
            max_score = max(max_score, front_score + rear_score)
        return max_score
      
      
