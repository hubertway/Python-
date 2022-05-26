a,n = input().split()
n = int(n)
sum = 0
x = ""
while n != 0:
    x = x + a + a
    n = n - 2
    sum = sum + int(x)
print(sum)
