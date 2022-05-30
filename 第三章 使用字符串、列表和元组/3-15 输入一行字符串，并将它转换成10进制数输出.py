s = input()
l = list(s)
i = 0
while i < len(l):
    if l[i] >= 'a' and l[i]<= 'f':
        i += 1
        continue
    elif l[i] >= 'A' and l[i]<= 'F':
        i += 1
        continue
    elif l[i] >= '0' and l[i]<= '9':
        i += 1
        continue
    else:
        del l[i]
x = "0x"+"".join(l)
print("".join(l))
print(int(x,16))
