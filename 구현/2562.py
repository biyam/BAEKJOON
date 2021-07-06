numList = []
for _ in range (9):
    num = int(input())
    numList.append(num)

numMax = max(numList)
print(numMax)

for i in range(9):
    if numMax == numList[i]:
        print(i+1)