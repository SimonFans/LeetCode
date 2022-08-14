MS OA:

# def fun1(arr):
#     res = 1
#     for num in arr:
#         res *= num
#     if res > 0:
#         return 1
#     elif res < 0:
#         return -1
#     else:
#         return 0

# test =[[1,1,1],[1,1,-1,],[1,1,0]]
# for t in test:
#     print(fun1(t))

# from collections import defaultdict
# def fun2(arr):
#     if not arr or len(arr) == len(set(arr)):
#         return 0
#     dist = float('-Inf')
#     dist_map = defaultdict(int)
#     for index, num in enumerate(arr):
#         if num not in dist_map:
#             dist_map[num] = index
#         else:
#             dist = max(dist, index - dist_map[num])
#     return dist

# test = [[1,1,2,3,4,2,1],[2,3,4,3],[1,2,3,4]]
# for t in test:
#     print(fun2(t))

#### delete 5
def fun3(num):
    if num == 0:
        return 0
    if num > 0:
        flag = 1
    else:
        flag = -1
    candidate_index, target_index = -1, -1
    res = ''
    num_str = str(abs(num))
    if num > 0:
        for i in range(len(num_str)):
            # current 5 is less than the next number, current i is the target delete index
            if num_str[i] == '5' and i < len(num_str) - 1 and int(num_str[i]) < int(num_str[i+1]):
                target_index = i
                break
            # current 5 is greater than the next number, continue to check if there's any
            # other 5 meets the above if condition. If not, delete the index of the last 5
            elif num_str[i] == '5':
                candidate_index = i
    else:
        for i in range(len(num_str)):
            if num_str[i] == '5' and i < len(num_str) - 1 and int(num_str[i]) > int(num_str[i+1]):
                target_index = i
                break
            elif num_str[i] == '5':
                candidate_index = i
    remove_index = candidate_index if target_index == -1 else target_index
    res = num_str[:remove_index] + num_str[remove_index+1:]
    return flag * int(res)


### fair index
#https://www.1point3acres.com/bbs/thread-884569-1-1.html

class Solution():
    def solution(self,A,B):
        count = 0
        sum_A = sum(A)
        sum_B = sum(B)
        left_A = 0
        left_B = 0
        for i in range(len(A)-1):
            left_A += A[i]
            left_B += B[i]
            if left_A == sum_A - left_A == left_B == sum_B - left_B: 
                count += 1
        return count
///
class solution():
    def countFairIndex(self, arr1, arr2):
        prefix_sum_arr1 = []
        prefix_sum_arr2 = []
        sum1 = 0
        sum2 = 0
        for num in arr1:
            sum1 += num
            prefix_sum_arr1.append(sum1)
        for num in arr2:
            sum2 += num
            prefix_sum_arr2.append(sum2)
        index, N = 0, len(arr1)
        count = 0
        while index < N - 1:
            if prefix_sum_arr1[index] == prefix_sum_arr1[N-1] - prefix_sum_arr1[index] \
            and prefix_sum_arr2[index] == prefix_sum_arr2[N-1] - prefix_sum_arr2[index] \
            and prefix_sum_arr1[index] == prefix_sum_arr2[index]:
                count += 1
            index += 1
        return count

A = [0, 4, -1, 0, 3]
B = [0, -2, 5, 0, 3]
print(solution().countFairIndex(A,B))
A = [2, -2, -3, 3]
B = [0, 0, 4, -4]
print(solution().countFairIndex(A,B))
A = [4, -1, 0, 3]
B = [-2, 6, 0, 4]
print(solution().countFairIndex(A,B))
A = [3, 2, 6]
B = [4, 1, 6]
print(solution().countFairIndex(A,B))
A = [1,4,2,-2,5]
B = [7, -2, -2, 2, 5] 
print(solution().countFairIndex(A,B))





https://www.1point3acres.com/bbs/thread-882811-1-1.html
(1)
def maxNumberEvenPairs(A):
    counter = 0
    c1, c2 = 0, 0 
    A.append(A[0])
    for i in range(0,len(A)-1,2):
        if (A[i] & 1) == (A[i+1] & 1):
            c1 += 1
    for i in range(1,len(A),2):
        if i < len(A) - 1 and (A[i] & 1) == (A[i+1] & 1):
            c2 += 1
    return max(c1,c2)

A = [[4,2,5,8,7,3,7],[14,21,16,35,22],[5,5,5,5,5]]
for t in A:
    print(maxNumberEvenPairs(t))

(2)
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # 连续4个人坐在一起，有通道的时候，必须两边各有两个人
        # 一行10个座位，最多4个连排的可能性是2个。N行最多连排的可能性是2*N
        # 两种方案：(1) 2,3,4,5 and 6,7,8,9. (2) 4,5,6,7
        seats = collections.defaultdict(set)
        total_possibility = 2 * n
        for i, j in reservedSeats:
            if j in (2,3,4,5):
                seats[i].add(0)
            if j in (4,5,6,7):
                seats[i].add(1)
            if j in (6,7,8,9):
                seats[i].add(2)
        for i in seats:
            # 没有连续四个的位置
            if len(seats[i]) == 3:
                total_possibility -= 2
            # 还有一个四人的位置
            else:
                total_possibility -= 1
        return total_possibility


https://www.1point3acres.com/bbs/thread-881036-1-1.html
(1)
def fun(N, K):
    num_str = str(N)
    new_str = ''
    i = 0
    while i < len(num_str):
        if 9 - int(num_str[i]) <= K:
            new_str += '9'
            K -= (9 - int(num_str[i]))
        else:
            new_str += str(int(num_str[i]) + K)
            break
        i += 1
    if i < len(num_str):
        new_str += num_str[i+1:]
    return int(new_str)

(2)
from collections import defaultdict
def countUniqueSubstr(st):
    hashMap = defaultdict(int)
    cnt = 1
    for s in st:
        if s in hashMap:
            cnt += 1
            hashMap.clear()
        hashMap[s] = 1
    return cnt

st = ['world','dddd','abba']
for t in st:
    print(countUniqueSubstr(t))


### move balance question to make sure all consecutive sum is positive
import heapq
def solution(A):
    total_sum = 0
    relocate_cnt = 0
    heap = []
    for i in range(len(A)):
        total_sum += A[i]
        if A[i] < 0:
            heapq.heappush(heap,A[i])
        if total_sum < 0:
            max_negative = heapq.heappop(heap)
            total_sum += abs(max_negative)
            relocate_cnt += 1
    return relocate_cnt

test = [[10,-10,-1,-1,10], [-1,-1,-1,1,1,1,1],[5,-2,-3,1]]
for t in test:
    print(solution(t))


# given a string, return the minimum umber of additional letters needed to obtain a string containing block of equal lengths
def solution(s: str) -> int:
    if not s:
        return 0
    
    groups = []
    prev, count = s[0], 1
    max_len = 0
    for c in s[1:]:
        if c == prev:
            count += 1
        else:
            groups.append(count)
            count = 1
            prev = c
        max_len = max(max_len, count)
    groups.append(count)
    max_len = max(max_len, count)
    
    return sum(max_len - group for group in groups)

print(solution("babaa")) # 3
print(solution("bbbab")) # 4
print(solution("bbbaaabbb")) # 0


### Maximum possible value by inserting '5'
def solution(num, k):
    if num >= 0:
        flag = 1
    else:
        flag = -1
    num_str = str(abs(num))
    new_str = ''
    if flag == 1:
        for i in range(len(num_str)):
            if int(num_str[i]) < 5:
                new_str = num_str[:i] + '5' + num_str[i:]
                break
    else:
        for i in range(len(num_str)):
            if int(num_str[i]) > 5:
                new_str = num_str[:i] + '5' + num_str[i:]
                break

    return int(new_str) * flag
              
num = 0    
print('xx',solution(num, 5))


#### MS Hiring event 3/8

1. A thread based question based on my experience in the resume
2. Maximum product subarray
3. System Design - Something like Google Search with certain restrictions
4. Longest common substring

1. OOP - Parking Garage, list noteworthy objects/classes. Given an entrance, implement a method to find the nearest parking spot. 
2. Coding: https://leetcode.com/problems/reverse-linked-list/ 
3.  System Design: Design a key-value store along with its possible interfaces: scale in steps: 
    1. start with in memory representation of key-value store
    2. We will then try to scale it for when the whole data can't fit in memory but can still fit in a node
    3. we will then scale a system that won' fit on one node but will need to be scaled across multiple nodes. (sharding, hashing) Had to implement methods for a dictionary/map, talk about scaling.
4.  Coding: Find the shortest distance between two people in a social network like LinkedIn.


1. Longest Substring with no repeating characters
2. Design a Maximum Frequency Stack -- https://leetcode.com/problems/maximum-frequency-stack/
3. Checking if a 2 values in an array add up to a third;
4. Write a function that takes an array of integers as input corresponding to the daily transactions of an account and returns the number of suspicious transactions where suspicious transactions are defined as: transactions that are 2x larger than the median transaction in the previous window of size W. Sample input: Arr = [100, 0, 200, 200, 500, 300, 650] W = 3

Sample output: 2
