number=int(input())
lst=list(map(int,input().split()))
k=sorted(lst)
for i in range(0,len(k)):
  print(k[i],end=" ")
