l = input().split()
for i in range(3):
    l[i] = int(l[i])
l.sort()
for i in range(2):
    print(chr(l[i]),end='<')
print(chr(l[2]))
