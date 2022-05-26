low,up = input().split()
low = int(low)
up = int(up)
if not (-20 <= low and low <= up and up <= 50):
    print("Invalid.")
else:
    print("celsius    fahr")
    while low <= up:
        print("{}{:>14}".format(low,low*1.8+32))
        low = low + 2
