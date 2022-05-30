s1 = input()
s2 = input()
d = {}
for i in s1:
    d[i] = 0
for i in s1:
    if d[i] > 0:
        d[i] += 1
    else:
        d[i] = 1

f = True
for i in s2:
    if i in d:
        d[i] -= 1
    else:
        print("no")
        f = False
        break
if f == True:
    for v in d.values():
        if v != 0:
            print("no")
            f = False
            break
    if f == True:
        print("yes")
