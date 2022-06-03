s = hex(int(input()))[2:]
x = input()
cnt = 0
for i in range(len(s)):
    if x == s[i]:
        cnt += 1
print(cnt)
