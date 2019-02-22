给个string，里面有各种括号和字符，看是否匹配（）[] {} <>...  

def valid_String(str):
    Map={')':'(',']':'[','}':'{','>':'<'}
    stack=[]
    if len(str)==0:
        return False
    for i in str:
        # 如果是非括号元素就继续
        if i.isalpha():
            continue
        # 如果stack为空，且遇到右侧括号，返回False
        if i in Map.keys() and len(stack)==0:
            return False
        # 如果遇到左侧括号，直接加入stack
        if i in ['(','{','[','<']:
            stack.append(i)
        # 否则当stack不为空时，取出stack最后一个，和当前的做比较，不匹配，返回False
        else:
            if len(stack)!=0:
                cur=stack.pop()
            if Map.get(i)!=cur:
                return False
    # 最后看stack是不是为空
    return len(stack)==0


print(valid_String("ab{<dd>}"))
