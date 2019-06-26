s1=list(input())
p=[]
for i in s1:
    if i not in p:
        p.append(i)
if s1==p:
    print("Yes")
else:
    print("No")
