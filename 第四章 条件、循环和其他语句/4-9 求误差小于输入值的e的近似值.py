er = float(input())
e1 = 1.0
e2 = 2.0
x = 2
while True:
    if e2 - e1  <= er:
        print("{:.6f}".format(e2))
        break
    e1 = e2
    m = 1
    for i in range(2,x+1):
        m *= i
    e2 += 1/m
    x += 1
