giving a str with alpha-numeric and parenthenes, output alpha-numeric and valid pair of parenthenes, e.g. ((((a)b)( =>((a)b)



def balance(st):
    temp =[]
    ok = []
    # 将非左括号和右括号的数字或字母的index放入最后便利的list中                                                                                                               
    for i, c in enumerate(st):        
        if c !='(' and c !=')':
            ok.append(i) 
            continue
         # 如果遇到右括号，[0,'('] or [0,')'], 第一种可以因为最后一位的左括号与之匹配，第二种不可以，只能暂时压入temp list
        if c ==')' :      
            if len(temp)>1 and temp[-1] =='(': # check if valid pair parentheses, if yes, save the index
                ok.append(i) 
                ok.append(temp[-2])
                temp.pop(-1) #remove the paired parentheses
                temp.pop(-1)
        else: #if '(' , temp save index and ( into stack
            temp.append(i)
            temp.append(c)
       # 最后遍历字符串，将满足条件的index找出来拼凑成新的字符串
    out =''
    for i, c in enumerate(st):
        if i in ok:
            out += c
    return out
