from math import floor
m,n = input().split()
n = int(n)
m = int(m)
sum = 0.0
while m <= n:
    sum = sum + m**2 + 1/m
    m = m + 1
print("sum ≈",floor(sum))
