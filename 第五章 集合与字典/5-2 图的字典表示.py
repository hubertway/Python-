n = int(input())
l = []
for i in range(n):
    l.append(eval(input()))
vn = n
en = 0
wn = 0
for i in range(n):
    for v in l[i]:
        for w in l[i][v].values():
            en += 1
            wn += w
print(vn,en,wn)
