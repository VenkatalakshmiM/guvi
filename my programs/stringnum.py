inp=input()
l=False
w=False
for i in inp:
  if i.isalpha()==True:
    l=True
  if i.isdigit()==True:
    w=True
if(l==True and w==True):
  print("Yes")
else:
  print("No")
