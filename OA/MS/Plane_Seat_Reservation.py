Refer to https://leetcode.com/discuss/interview-question/492652/

def plane_seat_reservation(n,s):
    res = 0
    h=dict()
    for i in range(1,n+1):
        h[i] = set()
    for v in s.split():
        h[int(v[0:-1])].add(v[-1])
    case1={'D','E','F','G'}
    case2={'B','C','D','E'}
    case3={'F','G','H','J'}
    case4={'A','K'}
    valid=[case1,case2,case3]
    for k,v in h.items():
        # if row is empty or only A and K is taken, we can accomodate 2 families
        temp = case4 ^ v  # if only A and K is taken, case4 ^ v will be empty
        # but if either only A or K is taken, we still accommodate 2 families
        if len(v) == 0 or len(temp) == 0 or (len(temp) == 1 and len(temp & {'A', 'K'}) == 1):
            res+=2
        # for any other case, can accomodate 1 family only
        elif any(case not in v for case in valid):
            res+=1
    return res

>>plane_seat_reservation(2, "1A 2F 1C")
2
>>> plane_seat_reservation(2, "1A 2F")
{1: {'A'}, 2: {'F'}}
3
>>> plane_seat_reservation(15, "11A 12F 10C 1A 2K 1D 3A 2A")
27
