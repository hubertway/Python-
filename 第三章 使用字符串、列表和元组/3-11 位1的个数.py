x = int(input())
n = bin(x)
s = str(n)
l = list(s)
cnt = 0
for i in range(len(s)):
    if l[i] == '1':
        cnt += 1
print(cnt)
