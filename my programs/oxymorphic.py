v,l=map(str,input().split())
if(len(v)!=len(l)):
 print("no")
else:
 s2=[v.count(i) for i in v]
 s3=[l.count(i) for i in l]
if(s2==s3):
 print("yes")
else:
 print("no")
