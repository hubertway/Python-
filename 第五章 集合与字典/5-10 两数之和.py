l = list(map(int,input().split(',')))
t = int(input())
f = False
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i] + l[j] == t:
            print("{} {}".format(i,j))
            f = True
if f == False:print("no answer")
