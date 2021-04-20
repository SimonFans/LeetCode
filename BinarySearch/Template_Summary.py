'''
Binary Search two principles:

1. Shrink the search scope every iteration ( or recursion )
2. Cannot exclude potential answers during each shrinking 

'''

# 1) 找一个准确值
循环条件： l <= r
缩减搜索空间： l = mid + 1 , r = mid - 1

# 2) 找一个模糊值 (比4大的最小数)
循环条件： l < r
缩减搜索空间： l = mid ,  r = mid - 1 OR if a[mid]<val: l = mid + 1, else r = mid
  
l, r = 0, len(arr)-1
while l < r:
  mid = l + (r-l)/2
  if arr[mid] < k:
    l = mid + 1
   else:
    r = mid
return l

# 3) 万用型 
循环条件： l < r - 1
缩减搜索空间： l = mid ,  r = mid 

