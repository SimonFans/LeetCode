def maxInserts(word):
    word = "b"+word+"b"
    idx = [i for i in range(len(word)) if word[i] != "a"]
    count = 0
    for i in range(1,len(idx)):
        diff = idx[i]-idx[i-1]-1
        if diff >= 3:
            return -1
        count+=2-diff
    return count


a = "aabab"
print maxInserts(a)
a = "dog"
print maxInserts(a)
a = "aa"
print maxInserts(a)
a = "baaaa"
print maxInserts(a)


