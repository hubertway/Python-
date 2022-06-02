n = int(input())
l = []
s = set()
for i in range(1,n+1): 
    l.append(i)
    s.add(i)
i = j = 0
while True:
    if len(s) == 1: break
    if ((j+1)%3 == 0):
        s.remove(l[i])
        l[i] = 0
        j = 0
    else:j += 1
    i += 1
    if i == len(l): i = 0
    while True:
        if l[i] != 0:break
        else : 
            i += 1
            if i == len(l): i = 0
for i in range(len(l)):
    if l[i]!=0:print(l[i])
