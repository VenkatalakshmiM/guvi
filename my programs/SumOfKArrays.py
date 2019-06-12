totalnumber=int(input())
summingnum=int(input())
arraynums=[]
for ii in range(1,totalnumber+1):
  arraynums.append(ii)
temporaynum=0
for temp in range(0,summingnum):
  temporaynum+=arraynums[temp]
print(temporaynum)
