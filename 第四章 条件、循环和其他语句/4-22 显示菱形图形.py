n = int(input())
for i in range(1,int(n/2)+1):
    print("{: ^11}".format('*'*(2*i-1)))
for i in range(int(n/2)+1,0,-1):
    print("{: ^11}".format('*'*(2*i-1)))
