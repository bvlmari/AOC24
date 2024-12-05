allLists = []
orderedLists = []
finalList = []

with open("/path/input2.txt","r") as file:
    rawList = file.readlines()


for x in rawList:
    allLists.append(list(map(int, x.split())))

for z in range(len(allLists)):
    if all(allLists[z][i] <= allLists[z][i + 1] for i in range(len(allLists[z]) - 1)) or all(allLists[z][i] >= allLists[z][i + 1] for i in range(len(allLists[z]) - 1)) != False:
        orderedLists.append(allLists[z])

for a in orderedLists:
    addList=True
    for b in range(0,len(a)-1):
        if abs(a[b] - a[b+1])>3 or abs(a[b] - a[b+1])==0:
            addList=False
            break
    if addList:
        finalList.append(a)

print(len(finalList))