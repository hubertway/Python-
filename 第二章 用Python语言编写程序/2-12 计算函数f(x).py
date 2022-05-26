import math
x = float(input())
y = math.sin(35*math.pi/180) + (math.exp(x) - 15*x)/(math.sqrt(x**4 + 1)) - math.log(7*x)
print("f({})={:.3f}".format(x,y))
