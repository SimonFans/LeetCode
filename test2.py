from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print(type(s))

d=defaultdict(list)
for key,value in s:
    d[key].append(value)
print(d.items())

t={}
for k,v in s:
    t.setdefault(k,[]).append(v)
print(t.items())