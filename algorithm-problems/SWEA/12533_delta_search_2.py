# 델타 검색 응용
dx = [-1, -2, 1, 2, -1, 1, 2, -2]
dy = [-2, -1, -2, -1, 2, 2, 1, 1]

for test_case in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    for i in range(N):
        for j in range(N):
            for k in range(len(dx)):
                ni = i + dx[k]
                nj = j + dy[k]
                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue
                res = arr[i][j] - arr[ni][nj]
                if res < 0:
                    res *= -1
                total += res

    print(f'#{test_case + 1} {total}')
