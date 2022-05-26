n = int(input())
sum = 0.0
z = 1
m = 1
for i in range(1,n+1):
    if i % 2 == 1:
        sum = sum + z/m
    else:
        sum = sum - z/m
    z = z + 1
    m = m + 2
print("{:.3f}".format(sum))
