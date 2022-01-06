# Python Question 1:
# Calculate the average word length. 
# For the given set of words return the average word length. 

#
def avg_word_length(x):
   words=x.split()
   word_lengths=[len(word) for word in words]
   avg_word_length=sum(word_lengths)/len(words)
   Return (avg_word_length)


# assert avg_word_length('') == None
# assert avg_word_length('ibm') == 3
# assert avg_word_length('ibm microsoft') == 6
# assert avg_word_length(' Hello World ') == 5
# assert avg_word_length('The movie ends with The-end') == 4.6
# print('passed')

# Python Question 2:
# Check if a given IP address is valid. 
# A valid IP address must be in the form of xxx.xxx.xxx.xxx, 
# where xxx is a number from 0-255

# For example: 
#           - 256.1.2.3 is not a valid IP address because the
#             first octet number is greater than 255
#           - 245.1.2 is not a valid IP address because 
#             it has only 3 octets

# Note: We recommend you do NOT use regex to solve this question 
# as it can be difficult and time consuming to debug. You may however, do
# so if you wish.

# def is_valid_IP(check_ip):
#     # Your code here

Def is_valid_ip(address):
       parts= address.split(“.”)
       
       If len(parts)!=4 
          Print (“IP address invalid!”)
          Return False 
      
       For part in parts
              If not isinstance(int(part),int):
              Print (“IP address invalid!”)
             Return False

             If int(part)<0 or int(part)>255
             Print (“IP address invalid!”)
             Return False
             
Print (“IP address invalid!”)
Return True
           

# assert is_valid_IP('') == False
# assert is_valid_IP('127.0.0.1') == True
# assert is_valid_IP('127.0.0.100') == True
# assert is_valid_IP('192.34.0.0.1') == False
# assert is_valid_IP('192.3.0.1') == True
# assert is_valid_IP('192.289.25.10') == False
# assert is_valid_IP('192.289.25') == False
# assert is_valid_IP('a12.A.29.5') == False
# print('passed')

# Python Question 3:
# Calculate the number of friends for each person
# given a relationship graph.
# 
#
# For example: 
#   The relationships amongst a set of friends
#   are shown in the graph below, where a line
#   between 2 nodes represents a friendship:
#
#                A ----- B ----- D
#                |       |
#                |       |
#                |       |
#                C ------/       E
#
#   This graph is represented as a list of
#   lists:
#      graph = [[A,B],[A,C],[C,B],[B,D],[E]]
#
#   The function "count_friends(graph)" should return
#   a dictionary object, where the Key is the
#   person's name and the Value is the number of
#   friends.
#     
#   In the above example, the function should
#   return the following output:
#     {'A': 2, 'B': 3, 'C': 2, 'D': 1, 'E': 0}

#def check_results(dict1, dict2):
#    if len(dict1.keys()) != len(dict2.keys()):
#        return 1
#    for i in dict1.keys():
#        if dict1[i] != dict2[i]:
#            return 1
#    return 0
#
#
#assert check_results(count_friends([['A'],['B'],['C'],['D'],['E']]), {'A': 0, 'C': 0, 'B': 0, 'D': 0, 'E': 0}) == 0
#assert check_results(count_friends([['A','B'],['C','D'],['E','F']]), {'A': 1, 'C': 1, 'B': 1, 'E': 1, 'D': 1, 'F': 1}) == 0
#assert check_results(count_friends([['A','B'],['A','C'],['A','D'],['E']]), {'A': 3, 'C': 1, 'B': 1, 'E': 0, 'D': 1}) == 0
#assert check_results(count_friends([['A','B'],['A','C'],['C','B']]), {'A': 2, 'C': 2, 'B': 2}) == 0
#assert check_results(count_friends([['A','B'],['A','C'],['C','B'],['B','D'],['E']]), {'A': 2, 'C': 2, 'B': 3, 'E': 0, 'D': 1}) == 0
#print('passed')

# Python Question 4:
"""
Write a function that returns the elements on odd positions (0
based) in a list
"""
def solution(input):
     c=[]
     For i in range (1,len(input),2):
           c.append(a.[i])
     Return c
     
assert solution([0,1,2,3,4,5]) == [1,3,5]
assert solution([1,-1,2,-2]) == [-1,-2]
"""
# Python Question 5:
Write a function that returns the cumulative sum of elements in a
list
"""
def solution(input):
      cu_list=[]
      length=len(input)
      cu_list=[sum(input[0:x:1]) for x in range(0,length+1)]
      Return cu_list[1:]

assert solution([1,1,1]) == [1,2,3]
assert solution([1,-1,3]) == [1,0,3]
"""
# Python Question 6:
Write a function that takes a number and returns a list of its
digits
"""
def solution(input):
      c=str(input)
      int_list=[]
      For i in range(len(c)):
            in_list.append(int(c[i]))

Print (int_list)



assert solution(123) == [1,2,3]
assert solution(400) == [4,0,0]
"""

# Python Question 7:
From: http://codingbat.com/prob/p126968
Return the "centered" average of an array of ints, which we'll
say is
the mean average of the values, except ignoring the largest and
smallest values in the array. If there are multiple copies of the
smallest value, ignore just one copy, and likewise for the
largest
value. Use int division to produce the final average. You may
assume
that the array is length 3 or more.
"""
def centered_average(nums):
     b=nums
     ma=max(b)
     mi=min(b)
     l=(len(b)-2)
     
     s=sum(b)-max-min
     avg=int(s/l)
      
     Return avg

Def centered_average(nums):
    sorted_list= sorted(nums)
     Return sum(sorted_list [1:-1]/(len(sorted_list)-2))


assert solution([1, 2, 3, 4, 100]) == 3
assert solution([1, 1, 5, 5, 10, 8, 7]) == 5
assert solution([-10, -4, -2, -4, -2, 0]) == -3

# Python Question 7:
Remove redundant data from a list 

Def remove_redudant_data(b):
      c=[]
      For i  in b:
            If i not in c:
               c.append(i)
      Return c

# Python Question 8:
Return the largest and smallest elements in a list 

Def max_elements(data):
      Return max(data)

Def min_elements(data):
      Return min(data)

max_element_list=max_element(a)
min_element_list=min_element(a)
print(max_element_in_list)
print(min_element_in_list)

# Python Question 9:
Python code to reverse an integer number

Def revese_number (input):
     num=str(input)
     reverse_number=num[::-1]

     reverse_number_int=int(reverse_number)

Print (reverse_number_int)

# Python Question 10:
Python code to print sum of first 100 Natural Numbers

Def sum_of_first_100_natural_number ():
       sum = 0 
       For i in range(1,101):
             sum=sum+i
Return sum


# Python Question 11:
Python | Count occurrences of a character in string
test_str = "GeeksforGeeks"
  
# using count() to get count 
# counting e 
counter = test_str.count('e')
  
# printing result 
print ("Count of e in GeeksforGeeks is : "  +  str(counter))

# Python Question 12:
Python | Replace NONE by its previous NON None value

def none_replace(ls):
    p = None
    return [p:=e if e is not None else p for e in ls]


x =[None, None, 1, 2, None, None, 3, 4, None, 5, None, None]
for i,e in enumerate(x[:-1], 1):
    if x[i] is None:
        x[i] = x[i-1]
print(x)


x =[None, None, 1, 2, None, None, 3, 4, None, 5, None, None] 
  for i in range(len(x)): 
        if x[i] is None: 
           x[i] =x[i-1]
  Print (x)


# Python Question 13:
given two lists output the words that don't exist in both lists

new_list = list(set(list1).difference(list2))

new_list = list(set(list1).intersection(list2))

# Python Question 14:
Python to find N largest elements from a list

Def top_n_elements (list1,N)
      l=list1.sort()
      Print (l[-n:])

# Python Question 15:
Python to find second largest number in  a list 
list1=[10,20,5,9,30]
l=list1.sort()
print(l[-2])

To print even number in a list 

list1 = [10, 21, 4, 45, 66, 93]
For num in list 1 
       If num%2 ==0
         Print (num,end=” ”)

Method 2
Even_num = [num for num in list1 if num % 2 ==0]

Print (even_num)

Print all even numbers in a range

start=int(input)
end=int(input)

For num in [start,end+1]:
       If num % 2 == 0 
           Print (num, end= “ ”)

Print all odd number in a range 
Start = int (input)
End = int (input)

For num in [start,end+1]:
       If num % 2 !=0 
          Print (num, end=” ”)

Print all odd number in a list 
odd_number= [number for number in list1 if num % 2 != 0]

Print (odd_number)

# Python Question 16:
Count Even and odd number in a list 
Odd_list = [num for num in list1 if num % 2 == 1]
odd_count= len (odd_list)
Even_count = len (list1)-odd_count

Print positive number in a list 

For num in list1:
   If num >=0 :
       Print (num, end “ ”)

Print negative number in a list 

For num in list1:
     If num < 0 :
      Print (num, end “ ”)

Count positive number and negative number in a list 
 
For num in list1:
      Positive_list = [num for num in list 1 if num>=0]
      Positive_list_count = len (positive_list) 
      Negative_list_count = len(list1) - positive_list_count)

# Python Question 17:
Remove empty tuples from a list 

 Def remove_empty_tuples (tuple):
        tuple=filter(none, tuples)
         Return tuple

Print duplicates from a list of integer 
l=[1,2,2,3,4,5]
l1=[]
For i in l 
       If i not in l1:
       l1.append(i)
else :
       Print (i,end= “ ”)

      coding 五道：一) 由于有给test case但有很多cornor case建议看完题后先处理cornor case，第一题问一句话里某个字符串重复的次数

char=str (input)
occurrence=char.count.(‘e’)

                           二）给两个包含数字的列表，求两个列表里不重复的数字，不用在意输出顺序
Difference_list = list(set(list1).difference(list2))
                           三）给一个数字列表且里面有None，重新输出一遍把None位置的数用前面存在的数代替
Def replace_non (ls)
      For i in range (len(ls):
            If ls[i] is none: 
                ls[i]=ls[i-1]
Return (ls)
               
                           四）给一个字典，求字典值里第N大的值的键
Def n_largest (dic,n)
sorted_dic=dic.sort()
Print (dic[-n])


                           五）给一个数字列表且某些数字重复，给出每个数字还需要加进多少个才能使得列表里每个数字都一样多



Given a two dimensional list, for example [ [2,3],[3,4],[5]] person 2 is friends with 3 etc, find how many friends each person has. Note, one person has no friends

def find_friends(lst): 
     dct = {} 
     for element1 in lst: 
          for element2 in element1:
          if len(element1) != 1: 
            dct[element2] = dct.get(element2,0) + 1 
          else: dct[element2] = 0 
return dct

Can you do the following without using subquery?: {1,None,1,2,None} --> [1,1,1,2,2] Ensure you take care of case input[None] which means None object
Def replace_none (dict):
      ls=list(dict)
      For i in ls:
            If ls[i] is none:
               ls[i]=dic[i-1]
Print (ls)

Complete a function that returns a list containing all the mismatched words (case sensitive) between two given input strings # For example: # - string 1 : "Firstly this is the first string" # - string 2 : "Next is the second string" # # - output : ['Firstly', 'this', 'first', 'Next', 'second']
str_1=””
str2=””
mismatched_words=list(set(str_1).difference(str-2))

Complete a function that returns the number of times a given character occurs in the given string.
# For example:
# - input string = "mississippi"
# - char = "s"
#
# - output : 4

input_str=” mmmm”
counter=input_str.count(‘s’)
Print (counter)

Given an array containing None values, fill in the None values with the most recent non None value in the array. For example:input array: [1,None,2,3,None,None,5,None] # - output array: [1,1,2,3,3,3,5,5]

Def replace_none (ls):
      For i in ls: 
   If ls[i] is none:
       Ls[i] = ls[i-1]
  Return (ls)


Given an array of integers, we would like to determine whether the array is monotonic (non-decreasing/non-increasing) or not. Examples:
 // 1 2 5 5 8 
// true 
// 9 4 4 2 2 
// true 
// 1 4 6 3 
// false  
//1 1 1 1 1 1
// true

def isMonotonic(A):
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
  
# Driver program
A = [6, 5, 4, 4]
  
# Print required result
print(isMonotonic(A))
  


Given two sentences, construct an array that has the words that appear in one sentence and not the other

Given an ip address as an input string, validate it and return True/False

Count the neighbors of each node in a graph. Input graph is a multi dimensional list
Def count_friends (input_graph):
    new_dict={}
    For element1 in input_graph: 
          For element2 in element1: 
       If len(element2) != 1
          dct[element2] = dct.get(element2,0) + 1           
Else return 0
         

Given a dictionary, print the key for the nth highest value present in the dict. If there are more than 1 record present for nth highest value then sort the key and print the first one
Flatten a nested dictionary
def nth_highest(inp,n):
b=list(sorted(set(inp.values()), reverse=True))
o={k for k,v in inp.items() if v==b[n-1]}
return min(o)

You have a 2-D array of friends like [[A,B],[A,C],[B,D],[B,C],[R,M], [S],[P], [A]]. Write a function that creates a dictionary of how many friends each person has. People can have 0 to many friends. However, there won't be repeat relationships like [A,B] and [B,A] and neither will there be more than 2 people in a relationship

What is a loop that goes on forever?
Infinite loop 

Recursively parse a string for a pattern that can be either 1 or 2 characters long

Write a simple spell-checking engine

Given two sentences, you have to print the words those are not present in either of the sentences.(If one word is present twice in 1st sentence but not present in 2nd sentence then you have to print that word too)

Question: Find overlapping interval:
                      
A = [[1,3],[5,7], [8,12]]
B = [[2,3],[4,9], [10,15]]
# return [(2, 3), (5, 7), (8, 9), (10, 12)]

m = len(A)
n = len(B)
ans = []
i, j = 0,0 
while i < m and j < n:
    # left bound for intersecting segment 
    l = max(A[i][0], B[j][0])
    # right bound for intersecting segment 
    r= min(A[i][1], B[j][1])
    if l <= r:
        ans.append((l,r))
    if A[i][1] < B[j][1]:
        i += 1
    else:
        j += 1
print(ans)
                      
                   
