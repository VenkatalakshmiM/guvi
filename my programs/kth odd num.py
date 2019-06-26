ji,k=input().split()
k=int(k)
m=list(map(int,input().split()))
h=[]

for i in range(0,len(m)):
    if m[i]%2!=0:
        h.append(m[i])
print(h[k-1])
