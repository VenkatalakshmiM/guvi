num1,num2=map(int,(input().split()))

for i in range(num1,num2+1):
  s=0
  temp=i
  while(temp>0):
    d=temp%10
    s=s+d**3
    temp=temp//10
  if(i==s and i>num1 and i<num2):
    print(i,end=" ")
  
 
