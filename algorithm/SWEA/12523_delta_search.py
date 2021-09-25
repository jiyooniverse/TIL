# 델타 검색
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for test_case in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < N and 0 <= nj < N:   # 반대로 포함 안 되는 경우를 걸러주는 방법(continue사용)
                    res = arr[i][j] - arr[ni][nj]
                    if res < 0:
                        res *= -1
                    total += res

    print(f'#{test_case + 1} {total}')