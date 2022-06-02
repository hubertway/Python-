m,n = map(int,input().split())
cnt = 0
for x in range(m,n+1):
    sum = 0
    l = []
    for i in range(1,int(x/2) +1):
        if x%i == 0:
            sum += i
            l.append(i)
    if sum == x:
        cnt += 1
        print("{} = ".format(x),end="")
        for j in range(len(l)):
            if j == len(l) - 1 : print(int(l[j]))
            else:
                print("{} + ".format(int(l[j])),end="")
if cnt==0 : print("None")
