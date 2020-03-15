def validLongestSubstring(s):
    if len(s)<3:
        return s
    cur,start=0,0
    end=1
    c=s[0]
    maxLen=1
    count=1
    
    while end < len(s):
        if s[end]==c:
            count+=1
            if count==2:
                if end-cur+1 > maxLen:
                    maxLen=end-cur+1
                    start=cur
            else:
                cur=end-1
        else:
            c=s[end]
            count=1
            if end-cur+1 > maxLen:
                    maxLen=end-cur+1
                    start=cur
        end+=1
                
    return s[start:start+maxLen]

s='aabbaaaaabb'
s1='aabbaabbaabbaa'
print(validLongestSubstring(s))
