N = int(input())
for x in range(1 , N+1):
    for y in range(1 , x+1):
        print("{}*{}={: <4d}".format(y,x,x*y),end="")
    print("")
