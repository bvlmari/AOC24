file = open("/path/input.txt","r")
list1=[]
list2=[]
res=0
rawList = file.readlines()
for x in rawList:
    y = x.split()
    var1 = int(y[0])
    var2 = int(y[1])
    list1.append(var1)
    list2.append(var2)

list1.sort()
list2.sort()

for x in range(len(list1)):
    res = res + abs(list1[x]-list2[x])

print(res)




    