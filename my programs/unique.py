n1=int(input())
lst=list(map(int,input().split()))
u=[]
for i in range(n1):
  for j in range(i+1,len(lst)):
    if(lst[j]==lst[i]):
      u.append(lst[i])

if len(u)==0:
  print("unique")
else:
  u.sort()
  k=set(u)
  print(k,end=" ")
