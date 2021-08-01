from sys import stdin
# 입력 받기 시작
n, k, d = map(int, stdin.readline().split())
array = []
for _ in range(k):
    array.append(list(map(int, stdin.readline().split())))
# 입력 받기 끝


# 도토리 개수 세는 함수 dotori(pivot)
# 여기까지 세었을 때 딱 d개가 저장된다!는 거를 알려고
def dotori(pivot):
    total = 0
    # array에 순서대로 시작값, 끝값, 도토리 넣는 간격을 입력받았었음.
    # array가 [[a, b, c], [d, e, f], ...]형태인데 
    # 아래의 for문이 모든 인덱스를 탐색해줌.
    for start, end, step in array:
        # 여기까지 있는 도토리가 몇개다! 
        # (최종적으로 위치를 찾으려고 하는 거니까)
        beta = min(end, pivot)
        if start <= beta:
            # 간격이 step일 때 start부터 beta까지 몇개가 있는지
            calc = (beta - start) // step + 1
            total += calc
    return total


# d번째 도토리 위치 찾는 함수 solution()
def solution():
    # 상자와 도토리 개수의 한계는 1000000
    start, end = 1, 1000000 
    ans = 0
    # 이진 탐색 시작
    while start <= end:
        # 계속 반으로 가르기
        mid = (start + end) // 2
        # 도토리 개수보다 크면 왼쪽 탐색
        if dotori(mid) >= d:
            ans = mid
            end = mid - 1
        # 도토리 개수보다 작으면 오른쪽 탐색
        else:
            start = mid + 1
    # start가 end보다 커지면 직전에 저장된 mid값을 
    # 결과값으로 return함
    return ans

# 출력
print(solution())