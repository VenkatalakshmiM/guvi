num=int(input())
n1,n2=map(int,input().split())
for i in range(n1,n2+1):
  if(num==i):
    print("yes")
    break
else:
  print("no")
