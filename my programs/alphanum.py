lis=input()
v=[]
for i in lis:
  if(i.isnumeric()):
    v.append(i)
print(*v,sep='')
