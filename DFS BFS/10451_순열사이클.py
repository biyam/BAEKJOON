case_num = int(input())
lst = []
for i in range(case_num):
    num = int(input())
    line = list(map(int, input().split()))
    lst.append(line)

print(lst)