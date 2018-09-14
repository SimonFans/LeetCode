dir1='/Users/simon/Desktop/test/a.txt'
dir2='/Users/simon/Desktop/test/b.txt'
dir3='/Users/simon/Desktop/test/c.txt'

new_len=1


with open(dir1, 'r') as file1:
    with open(dir2,'r') as file2:
        file1_lines=[line.rstrip() for line in file1]
        file2_lines=[line.rstrip() for line in file2]
        print(file1_lines) # file1中所有的数据
        print(file2_lines) # file2 中所有的数据
        m=len(file1_lines) # file1 的长度
        n=len(file2_lines) # file2 的长度
        res=file1_lines+file2_lines

        output=list(map(int,res)) # map list strings to integer
        output=sorted(output)  # sorted list
        print(output)
        for i in range(1,len(output)):

            if output[i-1]!=output[i]:
                output[new_len]=output[i]
                new_len+=1

        result=output[:new_len]
        print(result)
        with open(dir3,'w') as file3:
            for line in result:
                file3.write(str(line)+"\n")










