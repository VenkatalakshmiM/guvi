from itertools import combinations
n1,n2=input().split()
n2=int(n2)
l=[]
d=combinations(n1,len(n1)-n2)
for i in list(d):
  l.append("".join(i))
print(min(l))
