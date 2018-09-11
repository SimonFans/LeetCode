class solution(object):

    def palindromePairs(self,words):

        wmap = {y: x for x, y in enumerate(words)}
        ans=set()

        def isPalindrome(word):
            size=len(word)
            for x in range(size//2):
                if word[x]!=word[size-x-1]:
                    return False
            return True

        for idx,word in enumerate(words):
            if isPalindrome(word) and "" in wmap and word!="":
                bidx=wmap[""]
                ans.add((idx,bidx))
                ans.add((bidx,idx))
            rword=word[::-1]
            if rword in wmap:
                ridx=wmap[rword]
                if idx!=ridx:
                    ans.add((idx, ridx))
                    ans.add((ridx, idx))
            for x in range(1,len(word)):
                left,right=word[:x],word[x:]
                rleft,rright=left[::-1],right[::-1]
                if isPalindrome(left) and rright in wmap:
                    ans.add((wmap["rright"],idx))
                if isPalindrome(right) and rleft in wmap:
                    ans.add((idx,wmap[rleft]))
        return list(ans)



words = ["bat", "tab", "cat"]
test=solution()
print(test.palindromePairs(words))
