n1,n2=map(str,input().split())
if len(n1)==len(n2):
  for i in range(0,len(n1)):
    if n1[i]==n2[i]:
      print("yes")
      break
  else:
      print("no")
  
