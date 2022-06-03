n = int(input())
l=[]
for i in range(n):
    l.append(input().split())
    l[i] = list(map(int,l[i]))
rmax=[]
for i in range(n):rmax.append(max(l[i]))
cmin=[]
for j in range(n):
    m = 99999
    for i in range(n):
        if l[i][j]<m:m=l[i][j]
    cmin.append(m)

cnt = 0
for i in range(n):
    for j in range(n):
        if l[i][j]>= rmax[i] and l[i][j]<= cmin[j]:
            cnt += 1
print(cnt)
