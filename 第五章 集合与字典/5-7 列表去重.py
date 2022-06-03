l = eval(input())
r = []
d = {}
for i in range(len(l)): d[l[i]] = True
for i in range(len(l)):
    if d[l[i]] == True:
        r.append(l[i])
        d[l[i]] = False
for i in range(len(r)):
    print(r[i],end="")
    if i < len(r) -1:print(" ",end="")
