给个string，里面有各种括号和字符，看是否匹配（）[] {} <>...  

def valid_String(str):
    Map={')':'(',']':'[','}':'{','>':'<'}
    stack=[]
    if len(str)==0:
        return False
    for i in str:
        if i.isalpha():
            continue
        if i in Map.keys() and len(stack)==0:
            return False

        if i in ['(','{','[','<']:
            stack.append(i)
        else:
            if len(stack)!=0:
                cur=stack.pop()
            if Map.get(i)!=cur:
                return False

    return len(stack)==0


print(valid_String("ab{<dd>}"))
