x,y = input().split()
x = bin(int(x))[2:]
y = bin(int(y))[2:]
l = 0
if len(x)>len(y):
    l = len(y)
else: 
    l = len(x)
cnt = 0
i = 0
while l > 0:
    if x[len(x)-1-i] != y[len(y)-1-i]:
        cnt += 1
    l -= 1
    i += 1
while len(x)-1-i >= 0 :
    if x[len(x)-1-i] != '0':
        cnt += 1
    i += 1
while len(y)-1-i >= 0 :
    if y[len(y)-1-i] != '0':
        cnt += 1
    i += 1
print(cnt)
