N, K = map(int,input().split())
coin_list = []

for _ in range(N):
    coin = int(input())
    coin_list.append(coin)
coin_list.reverse()

cnt = 0
for i in coin_list:
    if K == 0:
        break
    else:
        cnt += K//i
        K %= i

print(cnt)
