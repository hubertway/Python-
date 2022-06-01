t,d = map(float,input().split())
sum = d*t
if d<250:
    sum = sum
elif d>=250 and d<500:
    sum = sum*0.98
elif d>=500 and d<1000:
    sum = sum*0.95
elif d>=1000 and d<2000:
    sum = sum*0.92
elif d>=2000 and d<3000:
    sum = sum*0.9
else: sum = sum*0.85
print("{:.0f}".format(sum))
