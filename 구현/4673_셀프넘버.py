lst = []
num = list(range(1,10001))
for i in range(1, 10001):
    sum = i
    for j in range(len(str(i))):
        sum += int(str(i)[j])
        lst.append(sum)
    lst_set = set(lst)
res = list(set(num) - lst_set)
print(res)