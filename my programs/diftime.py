hr,mins=list(map(int,input().split()))
hr1,min1=list(map(int,input().split()))
h=hr-hr1
m=mins-min1
if h<0:
  h=-h
if m<0:
  m=-m
print(h,m,end=" ")
