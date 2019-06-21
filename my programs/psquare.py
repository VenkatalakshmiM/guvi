import math
num1,num2=map(int,input().split())
k=num1*num2
res=math.sqrt(k)
if(int(res + 0.5) ** 2 == k):
  print("yes")
else:
  print("no")
