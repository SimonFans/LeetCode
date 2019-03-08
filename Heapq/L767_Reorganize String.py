Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500]

class Solution:
    def reorganizeString(self, S: str) -> str:
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        for nc, x in pq:
            if -nc > (len(S)+1)//2:
                return ''
        ans=[]
        while len(pq)>=2:
            nct1,ch1=heapq.heappop(pq)
            nct2,ch2=heapq.heappop(pq)
            ans.extend([ch1,ch2])
            if nct1+1:
                heapq.heappush(pq,(nct1+1,ch1))
            if nct2+1:
                heapq.heappush(pq,(nct2+1,ch2))
            
        return ''.join(ans)+(pq[0][1] if pq else '') 
        
     
