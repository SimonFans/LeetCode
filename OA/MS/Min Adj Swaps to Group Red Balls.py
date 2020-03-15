def solution(arr):
    res=count = 0
    flag = False
    for i in arr:
        if i == 'R':
            flag = True
            res += count
            count = 0
        else:
            if flag:
                count += 1
    return res
    
print(solution('WRRWWR'))
