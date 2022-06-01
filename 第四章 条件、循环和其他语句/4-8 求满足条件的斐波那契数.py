n = int(input())
a = b = 1
l = [1,1,]
i = 2
while True :
    l.append(a+b)
    t1 = a
    t2 = b
    a = t1 + t2
    b = a + t2
    if l[i]>n:
        print(l[i])
        break
    i += 1
  
