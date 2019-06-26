numb=int(input())
sum=1
while(numb>0):
  d=numb%10
  numb=numb//10
  sum*=d
print(sum)
