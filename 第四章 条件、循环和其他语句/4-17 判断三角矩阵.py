N = int(input())
for i in range(N):
    n = int(input())
    l = []
    for i in range(n):
        l.append(input().split())

    f = False
    for i in range(0,n):
        f1 = True
        for j in range(i+1,n):
            if int(l[i][j])!=0:
                f1 = False 
                break
        if (f1 == False):break
    else: 
        f = True
        print("lower triangular matrix")
        continue

    for j in range(0,n):
        f2 = True
        for i in range(j+1,n):
            if int(l[i][j]) != 0:
                f2 = False
                break
        if f2 == False:break
    else:
        f = True
        print("upper triangular matrix")
        continue

    if f == False:print("no")


