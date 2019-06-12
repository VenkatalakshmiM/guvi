number1=int(input())
number2=int(input())

for i in range(number1,number2):
  if(i==number1 or i==number2 or (i%2==0)):
    continue
  else:
    print(i)
