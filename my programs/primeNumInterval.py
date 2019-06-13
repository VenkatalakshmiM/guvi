x=input().split()
num1=int(x[0])
num2=int(x[1])
for k in range(num1,num2+1):
  if k>1:
    for i in range(2,k):
      if(k%i==0 or k==num1 or k==num2):
        break
    else:
      print(k,end=" ")
