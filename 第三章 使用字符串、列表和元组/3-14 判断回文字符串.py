s = input().lower()
l = list(s)
index = 0
while index < len(l):
    if l[index].islower() == False:
        del l[index]
    else: index += 1
f = True
index = 0
while index < len(l)/2:
    if l[index] != l[len(l)-1-index]:
        print("no")
        f = False
        break
    index += 1
if f == True:
    print("yes")
