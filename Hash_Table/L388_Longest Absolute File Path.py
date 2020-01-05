Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.


import collections

"""
len('\t')=1 !!!

troubleshooting case:
Let's assume sting s="dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"

['dir', '\tsubdir1', '\tsubdir2', '\t\tfile.ext']
name 3
length of i: 3
deep 0
defaultdict(<class 'int'>, {0: 0, 1: 4})
name 7
length of i: 8
deep 1
defaultdict(<class 'int'>, {0: 0, 1: 4, 2: 12})
name 7
length of i: 8
deep 1
defaultdict(<class 'int'>, {0: 0, 1: 4, 2: 12})
name 8
length of i: 10
deep 2
defaultdict(<class 'int'>, {0: 0, 1: 4, 2: 12})
20

"""

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_length=0
        path=collections.defaultdict(int)
        
        for i in input.split("\n"):
            name=i.lstrip("\t")
            # deep 即为有多少个'\t'
            deep=len(i)-len(name)
            if '.' in name:
                max_length=max(max_length,path[deep]+len(name))
            else:
                # +1 是因为要算上 '/', deep+1统计的是这一层+上一层总共的字数
                path[deep+1]=path[deep]+len(name)+1
        return max_length
    
    
  
