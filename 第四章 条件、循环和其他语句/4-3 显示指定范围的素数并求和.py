m,n = map(int,input().split())
a = 0
s = 0
for x in range(m,n+1):
    if x == 1: continue
    else:
        for i in range(2,x):
            if x%i == 0:
                break
        else:
            a += 1
            s += x
            print(x,end=" ")
            if a%5 == 0: print()

if a == 0 :print("amount=0 sum=0")
else: print("\namount={} sum={}".format(a,s))
