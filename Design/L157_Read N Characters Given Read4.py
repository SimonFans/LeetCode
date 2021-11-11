class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        
        file -> buf4 -> buf
        file -> buf
        read4() => everytime return 4 
        read4(buf4) => save 4 chars into buf ('s','s','s','s') or ('d','','','')
        """
        
        copied_chars = 0
        read_chars = 4
        buf4 = [''] * 4
        
        while copied_chars < n and read_chars == 4:
            # read chars into buf4 and return how many chars you read
            read_chars = read4(buf4)
            print(read_chars)
            for i in range(read_chars):
                # if copied chars == n
                if copied_chars == n:
                    return copied_chars
                buf[copied_chars] = buf4[i]
                copied_chars += 1
        return copied_chars
