a,b=map(str,input().split())
if a==b:
    print("0")
else:
    if (len(b)>len(a)):
       l=0
       l1=[]
       l2=[]
       l3=[]
       for i in a:
           l1.append(i)
       for i in b:
           l2.append(i)
       for i in range(0,len(l1)+1):
           if l1[i]==l2[i]:
               l3.append(l1[i])
               l=l+1
           else:
               break;
       for i in range(l,len(l2)):
           l3.append(l2[i])
       print(len(l2)-l)
    else:
      l1=[]
      l2=[]
      l3=[]
      l=0
      for i in a:
          l1.append(i)
      for i in b:
          l2.append(i)
      for i in range(0,len(b)):
          if l2[i]==l1[i]:
              l3.append(l1[i])
              l=l+1
          else:
              continue;
      if len(b)>1:
          for i in range(l,len(l1)):
              l3.append(l2[i])
          print(len(l2)-1)
      else:
        print(len(l1)-1)    
