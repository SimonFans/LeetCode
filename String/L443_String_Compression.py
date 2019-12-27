Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

 
Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 

Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
 

Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.


# using only O(1) extra space
# i: 更改后位置长度的下标
# j: 当前位置的下标
# counter: 统计字出现的字数

class Solution:
    def compress(self, chars: List[str]) -> int:
        n=len(chars)
        i=0
        counter=1
        for j in range(1,n+1):
            if j<n and chars[j-1]==chars[j]:
                counter+=1
            else:
                chars[i]=chars[j-1]
                i+=1
                if counter>1:
                    for m in str(counter):
                        chars[i]=m
                        i+=1
                counter=1
        return i
       
