n1,n2=map(int,input().split())
a=n1
b=n2
while(n2):
  n1,n2=n2,n1%n2
  c=(a*b)//n1
print(c)
