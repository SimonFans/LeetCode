Given a text txt[0..n-1] and a pattern pat[0..m-1], 
write a function search(char pat[], char txt[]) that prints all occurrences of pat[] and its permutations (or anagrams) in txt[]. 
You may assume that n > m. 
Expected time complexity is O(n)

1) Input:  txt[] = "BACDGABCDA"  pat[] = "ABCD"
   Output:   Found at Index 0
             Found at Index 5
             Found at Index 6
2) Input: txt[] =  "AAABABAA" pat[] = "AABA"
   Output:   Found at Index 0
             Found at Index 1
             Found at Index 4
             
class solution():
    def search(self,pat,txt):

        def compare(A,B):
            for i in range(Max):
                if A[i]!=B[i]:
                    return False
            return True

        Max=256
        # two places to store pattern & text 个数
        countP=[0]*Max
        countTW=[0]*Max
        M=len(pat)
        N=len(txt)
        for i in range(M):
            countP[ord(pat[i])]+=1
            countTW[ord(txt[i])]+=1
        for i in range(M,N):
            if compare(countP,countTW):
                print('index found: ',i-M)
            countTW[ord(txt[i])]+=1
            countTW[ord(txt[i-M])]-=1
        # 如果走到最后也满足
        if compare(countP,countTW):
            print('index found：',N-M)

txt = "BACDGABCDA"
pat = "ABCD"
print(solution().search(pat,txt))
