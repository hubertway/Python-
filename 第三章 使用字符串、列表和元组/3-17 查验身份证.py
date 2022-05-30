n = int(input())
l = []
for i in range(n):
    l.append(input())
f = True 
for i in range(n):
    if l[i][:-1].isdigit():
        m = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2'][sum([int(l[i][j]) * [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2][j] for j in range(17)]) % 11]
        if m != l[i][17]:
            f = False
            print(l[i])
    else:
        f = False
        print(l[i])
if f == True:
    print("All passed")
