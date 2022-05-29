t1=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
t2=t1[::-1]
l = list(input())
for i in range(len(l)):
    if l[i].isupper():
        for j in range(25):
            if l[i]==t1[j]:
                l[i] = t2[j]
                break
for i in range(len(l)):
    print(l[i],end="")
