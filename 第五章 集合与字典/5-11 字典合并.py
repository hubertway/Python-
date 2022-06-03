d1 = eval(input())
d2 = eval(input())
d3 = {}
s = set()
for k in d1:
    s.add(k)
    if k in d2:
        d3[k] = d1[k] + d2[k]
    else: d3[k] = d1[k]
for k in d2:
    s.add(k)
    if k not in d3:
        d3[k] = d2[k]
l1 = list(s)
l2=[]
for i in range(len(l1)):
    if type(l1[i]) != int:
        l2.append(ord(l1[i]))
    else:l2.append(l1[i])
l2.sort()
print("{",end="")
for i in range(len(l2)):
    if l2[i] not in d3:
        l2[i] = chr(l2[i])
        print('"{}":{}'.format(l2[i],d3[l2[i]]),end="")
    else: print("{}:{}".format(l2[i],d3[l2[i]]),end="")
    if i <len(l2)-1:print(",",end="")
print("}")
