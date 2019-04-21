The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

class Solution:
    def countAndSay(self, n: int) -> str:
        
        seq="1"
        # take n=4 example, loop 3 times get final result on line input id=4
        for _ in range(n-1):
            seq=self.getNext(seq)
        return seq
    
    def getNext(self,seq):
        i,next_seq=0,""
        while i < len(seq):
            counter=1
            # no overfill, and count how many same char
            while i<len(seq)-1 and seq[i]==seq[i+1]:
                counter+=1
                i+=1
            next_seq+=str(counter)+seq[i]
            i+=1
        return next_seq
