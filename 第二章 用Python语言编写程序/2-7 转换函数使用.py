a,b = input().split(",")
b = int(b)
d = 0
sum = 0
for i in a[::-1]:
    sum = sum + int(i) * b**d
    d = d + 1
print(sum)
