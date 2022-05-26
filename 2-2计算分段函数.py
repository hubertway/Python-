x = float(input())
if x == 0:
    print("g({:.3f}) = 0.000".format(x))
else:
    print("g({:.3f}) = {:.3f}".format(x,1/(2*x)))
