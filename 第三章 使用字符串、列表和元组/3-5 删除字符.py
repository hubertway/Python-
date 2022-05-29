x=input().strip()
a=input().strip()
y = list(x)
l = len(y)
i = 0
while i < l:
    if y[i]==a or y[i]==a.upper() or y[i]==a.lower():
        del y[i]
        l -=1
        continue
    i += 1
print("result:",end=" ")
for i in range(len(y)):
    print(y[i],end="")
