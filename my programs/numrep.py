num,k=map(int,input().split())
lst=list(map(int,input().split()))
c=0
for i in lst:
  if i==k:
    c=c+1
print(c)
