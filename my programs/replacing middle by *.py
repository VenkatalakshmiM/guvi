num=input()
if(len(num)%2==0):
  num[int(len(num)/2)] ='*'
  num[int(len(num)/2)-1]='*'
else:
    num[int(len(num)/2)] ='*'
for i in range(0,len(num)):
    print(num[i],end='')
