m,n = map(int,input().split())
l = []
for i in range(m):
    l.append(input().split())
lt=[]
for j in range(n):
    s=""
    for i in range(m):
        s = s+ l[i][j]+" "
    lt.append(s.split())
for i in range(n):
    for j in range(m):
        print(lt[i][j],end="")
        if j < m-1 : print(" ",end="")
    print("")
        

