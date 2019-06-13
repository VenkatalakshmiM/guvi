num1=int(input())
num2=int(input())
for k in range(num1,num2+1):
  if k>2:
    for i in range(2,k):
      if(k%i==0):
        break
    else:
      if(k!=num1 or k!=num2):
        print(k)
