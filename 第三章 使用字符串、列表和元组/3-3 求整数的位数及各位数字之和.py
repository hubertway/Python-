x = input()
print(len(x),end=" ")
sum = 0
l = list(x)
for i in range(len(x)):
    sum += int(l[i])
print(sum)
