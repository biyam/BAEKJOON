# ATM 문제 - 백준 11399번

# 누적으로 더하니까 앞자리에 설수록 시간이 적게 걸려야 함.
n = int(input())
n_list = list(map(int,input().split()))
n_list.sort()
sum = 0
for i in range(len(n_list)):
    v = n_list[i]*(len(n_list)-i)
    sum += v
print(sum)
