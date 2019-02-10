Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

class Solution:
    def restoreIpAddresses(self, s: 'str') -> 'List[str]':
        res=set()
        path=""
        fields=4
        self.helper(s,res,path,fields)
        return list(res)
        
    def helper(self,s,res,ip,fields):
        if fields==0:
            if not s and ip not in res:
                res.add(ip[:-1])
            return
        
        for i in range(1,4):
            if i<=len(s):
                chunk=s[:i]
                if i==1:
                    self.helper(s[i:],res,ip+chunk+'.',fields-1)
                elif i==2 and s[0]!='0':
                    self.helper(s[i:],res,ip+chunk+'.',fields-1)
                elif i==3 and s[0]!='0' and int(chunk)<=255:
                    self.helper(s[i:],res,ip+chunk+'.',fields-1)
