num=int(input())
if(num==1):
  print("1")
elif(num==2):
  print("1 1")
else:
  t1=1
  t2=1
  print(t1,t2,end=" ")
  for i in range(3,num+1):
    res=t1+t2
    print(res,end=" ")
    t1=t2
    t2=res
