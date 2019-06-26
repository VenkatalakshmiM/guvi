n=input()
l=[]
k=[]
for i in range(0,len(n)):
  if i%2==0:
    l.insert(i,n[i])
  else:
    k.insert(i,n[i])
print(''.join(map(str,l)),end=" ")
print(''.join(map(str,k)),end=" ")
