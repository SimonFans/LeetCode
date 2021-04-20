'''
Binary Search two principles:

1. Shrink the search scope every iteration ( or recursion )
2. Cannot exclude potential answers during each shrinking 

'''

# 1) 找一个准确值
循环条件： l <= r
缩减搜索空间： l = mid + 1 , r = mid - 1

# 2) 找一个模糊值 
# case 1: (比4大的最小数)
循环条件： l < r
缩减搜索空间： l = mid ,  r = mid - 1 OR if a[mid]<val: l = mid + 1 else r = mid
  
l, r = 0, len(arr)-1
while l < r:
  mid = l + (r-l)/2
  if arr[mid] < k:
    l = mid + 1
   else:
    r = mid
return l

# case 2: (找数字2最后出现的)
l, r = 0, len(arr)-1
while l < r:
  mid = l + (r - l + 1)/2
  if arr[mid] > k:
    r = mid - 1
   else:
    l = mid
return l

# 3) 万用型 
循环条件： l < r - 1
缩减搜索空间： l = mid ,  r = mid 
# ( 找closest to 一个数字的 )
l, r = 0, len(arr) - 1
while l < r - 1:
  mid = l + (r - l)/2
  if arr[mid] < k:
    l = mid
   else:
    r = mid
# 这时候只剩下两个数字，分情况讨论k处于最前，中和最后位置的情况
if arr[r] < k:
  return r
elif arr[l] > k:
  return l
else:
  return l if k - arr[l] < arr[r] - k else r






