number1=int(input())
if(number1>1):
  for i in range(2,number1):
    if(number1%i==0):
      print("no")
      break
  else:
    print("yes")
      
else:
  print("no")
