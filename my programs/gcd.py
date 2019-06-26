n1,n2=map(int,input().split())
i = 1
while(i <= n1 and i <= n2):
    if(n1 % i == 0 and n2 % i == 0):
        gcd = i
    i = i + 1
print(gcd)
