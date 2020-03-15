class Solution():
    def solution(self,N):
        if N < 0:
            """
            -999 ---> [9,9,9] ---->[-5,9,9,9]
            -126 ---> [1,2,6] ---->[-1,2,5,6]
            """
            s = [x for x in str(N)[1:]]
            output = []
            for i in range(len(s)):
                if int(s[i]) < 5:
                    output.append(s[i])
                else:
                    output.append(str(5))
                    break
            #print(s[i],output)
            output.extend(s[i:])
            #print(int(''.join(output)))
            return - int(''.join(output))
        else:
            s = [s for s in str(N)]
            #print(s)
            output = []
            for i in range(len(s)):
                if int(s[i]) < 5:
                    output.append(str(5))
                    #print(output)
                    break
                else:
                    output.append(s[i])
            output.extend(s[i:])
            #print(output)
            return int(''.join(output))
s = Solution()
assert s.solution(-999) == -5999
assert s.solution(-268) == 5268
assert s.solution(670) == 6750
assert s.solution(0) == 50

print("pass all test case")
