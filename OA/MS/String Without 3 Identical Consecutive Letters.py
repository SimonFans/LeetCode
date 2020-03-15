def minDeletes3Consecutive(word):
    if len(word) < 3:
        return word
    prev = word[0]
    count = 1
    ret = word
    i = 1
    while i < len(ret):
        if ret[i] == prev:
            count +=1
        else:
            prev = ret[i]
            count = 1
        if count > 2:
            ret = ret[:i] + ret[i+1:]
            count -= 1
        else:
            i+=1
    return ret

print(minDeletes3Consecutive("eedaaad"))
print(minDeletes3Consecutive("xxxtxxx"))
print(minDeletes3Consecutive("uuuuxaaaaxuuu"))
