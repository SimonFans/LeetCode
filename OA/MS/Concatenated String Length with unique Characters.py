from itertools import permutations

def concatenated (A) :
    maxlen = 0
    for pair in permutations(A, r=2):
        temp = ''.join(pair)
        c = Counter(Counter(temp).values())
        print("c",c)
        if [ x for x in c.keys() if x > 1] :
            continue
        maxlen = max(maxlen, len(temp))
    return maxlen


A = ["co","dil","ity"]
print(concatenated(A))
for pair in permutations(A, r=2):
    print(pair)

