n = int(input())
tri=[0]*n
for i in range(n):
    tri[i]=[0]*(i+1)
    tri[i][0]=1
    tri[i][i]=1
    for j in range(1,i):
        tri[i][j]=tri[i-1][j-1]+tri[i-1][j]
for i in range(n):
    for j in range(i+1):
        print(tri[i][j],end=" ")
    print()
