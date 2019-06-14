num1=int(input())
lst=list(map(int,input().split()))
for i in range(0,len(lst)):
  print(lst[i],lst.index(lst[i]))
