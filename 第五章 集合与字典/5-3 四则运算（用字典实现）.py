x=float(input())
p=input()
y=float(input())
dic={'+':'x+y','-':'x-y','*':'x*y','/':'x/y'}
if p=='/' and y==0:
    print("divided by zero")
else:
  print(f"{eval(dic[p]):.2f}")
