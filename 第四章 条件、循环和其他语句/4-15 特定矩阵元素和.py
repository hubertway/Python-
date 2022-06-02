n = int(input())
l = []
for i in range(n):
    l.append(input().split())
sum = 0.0
for i in range(n):
    for j in range(n):
        if i==j or i+j == n-1:
            sum += float(l[i][j])
print("{:.2f}".format(sum))
