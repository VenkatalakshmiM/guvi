numb=int(input())
s=0
temp=numb
while(temp>0):
  d=temp%10
  s=s+d**3
  temp=temp//10
if(numb==s):
  print("yes")
else:
  print("no")
