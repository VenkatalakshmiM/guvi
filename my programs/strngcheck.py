num,k=map(int,input().split())
lst=list(map(int,input().split()))
c=0
for i in lst:
  if i==k:
    c=c+1
if c==0:
  print("no"
else:
  print("yes")
