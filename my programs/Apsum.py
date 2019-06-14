n1,a1,d1=map(int,input().split())
sum1=0
k=0
while k<n1:
  sum1=sum1+a1
  a1=a1+d1
  k=k+1
print(sum1)
