M,N = map(int,input().split())
l = []
for i in range(M):
    l.append(input().split())
f = False
for i in range(1,M-1):
    for j in range(1,N-1):
        if (int(l[i][j])> int(l[i-1][j]) and int(l[i][j])> int(l[i+1][j])
         and int(l[i][j])>int(l[i][j+1]) and int(l[i][j])> int(l[i][j-1])):
          print(int(l[i][j]),i+1,j+1)
          f = True
if f == False:print("None",M,N)
