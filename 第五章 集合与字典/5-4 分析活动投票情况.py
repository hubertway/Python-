l = input().split(',')
d={}
#for i in range(1,11):d[i] = 0 
for i in range (len(l)):
    d[int(l[i])] = d.get(int(l[i]),0) +1
r = []
for i in range(6,11):
    if i not in d:r.append(i)
for i in range(len(r)):
    print(r[i],end="")
    if i < len(r)-1: print(" ",end="")
