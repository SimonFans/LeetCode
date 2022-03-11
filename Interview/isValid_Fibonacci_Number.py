def create_fibonacci(n):
    if n in cache:
        return cache[n]
    if n == 1 or n == 2:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        cache[n] = result
        return result
    
def binarySearch(fibo, target):
    left, right = 0, len(fibo)-1
    while left <= right:
        mid = left + (right - left)//2
        if fibo[mid] == target:
            return True
        elif fibo[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

fibo = []
cache = {}
target = 8
for i in range(1, 101):
    fibo.append(create_fibonacci(i))
print(binarySearch(fibo, target))
