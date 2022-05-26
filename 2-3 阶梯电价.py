a,x = input().split()
a=float(a)
x=float(x)
if a <= 50:
    print("cost = {:.2f}".format(a*0.53))
else:
    print("cost = {:.2f}".format((a-50)*(0.53+x)+50*0.53))
