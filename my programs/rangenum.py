num=int(input())
c=0
for i in range(1,11):
  if(num==i):
    c=c+1
    break
if(c==0):
  print("no")
else:
  print("yes")
