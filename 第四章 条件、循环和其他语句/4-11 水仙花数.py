n = int(input())
for i in range (10**(n-1) , 10**n ):
    l = list(str(i))
    sum = 0
    for j in range(len(l)):
        sum += int(l[j])**n
    if sum == i:print(sum)    
