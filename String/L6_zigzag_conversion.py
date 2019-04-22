The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if given numRows==1 or given rows >= len(s)
        if numRows == 1 or numRows >= len(s):
            return s
        
        # store results
        zigzag=['' for i in range(numRows)]
        
        # row: start row, step: +1 or -1
        row,step=0,1
        
        for c in s:
            zigzag[row]+=c
            
            # reach top turn step to 1
            if row==0:
                step=1
            
            # reach to bottom turn step to -1
            elif row==numRows-1:
                step=-1
                
            row+=step
            
        return ''.join(zigzag)
        
# ''.join(zigzag) // insert '','#' in between two strings inside a list
# zigzag=['aa','bb']
# 'aabb'   

