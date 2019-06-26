num1=int(input())
liss=list(map(int,input().split()))
for i in range (len(liss)):
  if(liss[i]>liss[i+1]):
    break
print(i)
