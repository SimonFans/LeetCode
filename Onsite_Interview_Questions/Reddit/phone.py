import random

def fun():
    cnt = 0
    stack = []
    visited = [0] * 52
    cards = [(v,s) for s in ['Heart', 'Spade', 'Clubs', 'Dimand'] for v in [str(i) for i in range(2, 11)] + list("JKQA")]
    cards_pos = []
    for i, v in enumerate(cards):
        cards_pos.append((i,v))
    while 1:
        withdraw = random.choice(cards_pos) 
        # if it does not pick up
        if visited[withdraw[0]] != 1:
            if not stack:
                stack.append(withdraw[1][0])
            else:
                print(withdraw)
                if withdraw[1][0] == stack[-1]:
                    break
                else:
                    stack.append(withdraw[1][0])
            visited[withdraw[0]] = 1
            cnt += 1
    return cnt
print(fun())
