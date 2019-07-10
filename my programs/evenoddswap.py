x1=input()
l=len(x1)
s=""
for i in range (l):
  if((i%2)==0):
    s+=x1[i+1]
  else:
    s+=x1[i-1]
print (s)
