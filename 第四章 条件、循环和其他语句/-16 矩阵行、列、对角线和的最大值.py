s = input()
r = list(s.split(" "))
l = [[],[],[]]
x = 0
for i in range(3):
    for j in range(3):
        l[i].append(int(r[x]))
        x += 1
mxs = 0
for i in range(3):
    x = 0
    for j in range(3):
        x += l[i][j]
    if mxs < x: mxs = x
for i in range(3):
    x = 0
    for j in range(3):
        x += l[j][i]
    if mxs < x: mxs = x
x = 0
for i in range(3):
    for j in range(3):
        if i==j : x += l[i][j]
if mxs < x: mxs = x
x = 0
for i in range(3):
    for j in range(3):
        if i+j == 2 : x += l[i][j]
if mxs < x: mxs = x
print(mxs)
