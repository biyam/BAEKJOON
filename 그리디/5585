# 백준 5585번 거스름돈
# (500, 100, 50, 10, 5, 1)엔 x n개
# 1000엔을 내고 380엔을 사면 거스름돈은 1000 - 380 = 620엔

n = int(input())
charge = 1000 - n # 620
cnt = 0
while charge != 0:
    if charge // 500 >= 1:
        cnt += charge // 500 
        charge %= 500
    elif charge // 100 >= 1:
        cnt += charge // 100 
        charge %= 100
    elif charge // 50 >= 1:
        cnt += charge // 50
        charge %= 50
    elif charge // 10 >= 1:
        cnt += charge // 10 
        charge %= 10
    elif charge // 5 >= 1:
        cnt += charge // 5
        charge %= 5
    else: 
        cnt += charge // 1
        charge %= 1
print(cnt)
