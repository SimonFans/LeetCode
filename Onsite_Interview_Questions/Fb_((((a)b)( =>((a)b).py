giving a str with alpha-numeric and parenthenes, output alpha-numeric and valid pair of parenthenes, e.g. ((((a)b)( =>((a)b)



def balance(st):
    temp =[]
    ok = []
    for i, c in enumerate(st):
        if c !='(' and c !=')':
            ok.append(i) 
            continue

        if c ==')' :
            if len(temp)>1 and temp[-1] =='(': # check if valid pair parentheses, if yes, save the index
                ok.append(i) 
                ok.append(temp[-2])
                temp.pop(-1) #remove the paired parentheses
                temp.pop(-1)
        else: #if '(' , temp save index and ( into stack
            temp.append(i)
            temp.append(c)

    out =''
    for i, c in enumerate(st):
        if i in ok:
            out += c
    return out
