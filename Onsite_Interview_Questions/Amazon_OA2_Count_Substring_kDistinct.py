Count number of substrings with exactly k distinct characters
Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that has exactly k distinct characters.
Examples:

Input: abc, k = 2
Output: 2
Possible substrings are {"ab", "bc"}

Input: aba, k = 2
Output: 3
Possible substrings are {"ab", "ba", "aba"}

Input: aa, k = 1
Output: 3



class solution():
    def countkDistinct(self,str,k):
        n=len(str)
        # result
        res=0
        # store count of characters
        cnt=[0]*26
        # consider all substrings starts with str[i]
        for i in range(n):
            dis_count=0
            # initialize array
            cnt = [0] * 26
            for j in range(i,n):
                if cnt[ord(str[j])-97]==0:
                    dis_count+=1
                cnt[ord(str[j])-97]+=1
                if dis_count==k:
                    res+=1
                if dis_count>k:
                    break
        return res


str="aba"
print(solution().countkDistinct(str,2))
