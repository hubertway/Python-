l1 = input().split()
l2 = input().split()
s1 = set(l1)
s2 = set(l2)
s3 = s1 - s2
s4 = s2 - s1
cnt1 = 0
for i in range(len(l1)):
    if l1[i] in s3:
        print(l1[i],end="")
        cnt1 += 1
        if cnt1 <= len(s3):print(" ",end="")
cnt2 = 0
for i in range(len(l2)):
    if l2[i] in s4:
        print(l2[i],end="")
        cnt2 += 1
        if cnt2 < len(s4):print(" ",end="")
