s = input()
a,b=input().split(" ")
for i in range(len(s)):
    if s[len(s) - 1 - i]==a:
        print(len(s) - 1 - i , a)
    elif s[len(s) - 1 - i]==b:
        print(len(s) - 1 - i , b)
