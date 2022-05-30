s = input()
x = max(s)
t = tuple(s)
index = 0
for i in range(len(t)):
    if t[i] == x:
        index = i
print(x,' ',index)
