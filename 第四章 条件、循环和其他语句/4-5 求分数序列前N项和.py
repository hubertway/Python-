n = int(input())
sum = 0.0
z = 2
m = 1
for i in range(n):
    sum += z/m
    t1 = z
    t2 = m
    z = t1 + t2
    m = t1
print("{:.2f}".format(sum))
