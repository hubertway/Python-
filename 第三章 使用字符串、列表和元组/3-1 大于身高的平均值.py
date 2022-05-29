l = input().split(" ")
sum = 0
for i in range(len(l)):
    sum = sum + int(l[i])
avg = sum / len(l)
for i in range(len(l)):
    if int(l[i]) > avg:
        print(l[i],end=" ")
