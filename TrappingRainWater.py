"""

              *
      *       * *   *
  *   * *   * * * * * *
0 1 2 3 4 5 6 7 8 9 0 1

l                     r
"""

class solution:

    def trap(self,height):

        left,right=0,len(height)-1
        leftMax,rightMax=0,0
        res=0
        while left<right:
            if height[left]<height[right]:
                leftMax=max(height[left],leftMax)
                res+=leftMax-height[left]
                left+=1
            else:
                rightMax=max(height[right],rightMax)
                res+=rightMax-height[right]
                right-=1
        return res

test=solution()
height=[0,1,0,2,1,0,1,3,2,1,2,1]
print(test.trap(height))