import math
n = int(input())
sum = 0.0
while n > 0:
    sum = sum + 1/n
    n = n - 2
print("sum ≈",math.ceil(sum))
