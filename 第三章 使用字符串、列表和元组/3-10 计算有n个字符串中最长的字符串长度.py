n = int(input())
l = []
for i in range(n):
    l.append(input().strip())
cnt = 0
for i in range(len(l)):
    if len(l[i]) > cnt:
        cnt = len(l[i])
print("length={}".format(cnt))
