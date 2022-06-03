s1 = input()
s2 = input()
d={}
for i in range(len(s1)):
    d[s1[i]] = d.get(s1[i],0) + 1
if s2 in d:print(d[s2])
else:print(0)
