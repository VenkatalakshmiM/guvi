import statistics
num1=int(input())
lst=list(map(int,input().split()))
k=statistics.median(lst)
print(k)
