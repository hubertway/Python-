N = int(input())
l = input().split()
r = list(map(int,l))
r.sort()
d={}
for i in range(len(r)):d[r[i]] = d.get(r[i],0) + 1
for k,v in d.items():
    print("{}:{}".format(k,v))
