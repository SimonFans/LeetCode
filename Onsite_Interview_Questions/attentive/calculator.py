def parse(expression):
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    stack = []
    result = None
    while tokens:
        token = tokens.pop(0)
        if token == '(':
            stack.append([])
        elif token == ')':
            subexpression = stack.pop()
            if stack:
                print('before:', stack)
                stack[-1].append(evaluate(subexpression))
                print('after:', stack)
            else:
                result = evaluate(subexpression)
        else:
            stack[-1].append(token)

    return result


def evaluate(subexpression):
    ops = subexpression[0]
    args = []
    for arg in subexpression[1:]:
        if str(arg).isdigit() or (str(arg)[0] == '-' and str(arg)[1:].isdigit()):
            args.append(int(arg))
    if ops == 'ADD':
        return sum(args)
    elif ops == 'MULT':
        r = 1
        for arg in args:
            r *= arg
        return r
    else:
        raise ValueError("Unknown ops:{}".format(ops))

print(parse("(MULT 3 (ADD 3 4 ))"))
