er = float(input())
m1 = 1
m2 = 1+1/4
s = 3
while True:
    if abs(m2-m1) <= er:
        print("{:.6f}".format((6*m1)**0.5))
        break
    m1 = m2
    m2 += 1/s**2
    s += 1

    
