# E, S, M: 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19
# 가장 빠른 연도 출력

E, S, M = map(int,input().split())
for i in range(7981):
    if i % 15 == E and i % 28 == S and i % 19 == M:
        print(i)
        