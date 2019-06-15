num=int(input())
res=(num&(num-1))
if res==0:
  print("yes")
else:
  print("no")
