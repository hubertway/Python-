a = int(input())
b = int(input())
c = a + b
print("{:08}".format(int(bin(a)[2:])))
print("{:08}".format(int(bin(b)[2:])))
print("--------")
print("{:08}".format(int(bin(c)[2:])))
