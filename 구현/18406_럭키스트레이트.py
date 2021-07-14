a = input()
lst = []
lst.append(a[:len(a)//2])
lst.append(a[len(a)//2:])

sum1 = 0
sum2 = 0
for i in range(len(a)//2):
    sum1 += int(lst[0][i])
    sum2 += int(lst[1][i])
if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")

'''
num = input()
n = len(num) // 2
a = 0
b = 0
for i in num[:n]:
    a += int(i)
for i in num[n:]:
    b += int(i)
if a == b:
    print("LUCKY")
else:
    print("READY")
'''