n = int(input())
lst = list(map(int,input().split()))

sum = 0
sum_l = []
for i in lst:
    for j in lst:
        if i - j >= 0:
            sum += (i - j)
            sum_l.append(sum)
        else: 
            sum += (j - i)
            sum_l.append(sum)
    print(min(sum_l))