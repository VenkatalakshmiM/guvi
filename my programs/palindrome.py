number=int(input())
temp=number
revnum=0
while temp!=0:
  revnum=(revnum*10)+(temp%10)
  temp=temp//10
if number==revnum:
  print("yes")
else:
  print("no")
