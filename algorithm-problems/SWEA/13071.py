# 13071 화물 도크
def dfs(now, cnt):
    global total
    if cnt > total:
        total = cnt

    end = schedule[now][1]
    for i in range(now, N):
        if end <= schedule[i][0]:
            dfs(i, cnt + 1)


T = int(input())
for tc in range(T):
    N = int(input())
    schedule = [list(map(int, input().split())) for _ in range(N)]
    # 완료 시간이 빠른 순서로
    for i in range(N - 1):
        for j in range(i + 1, N):
            if schedule[i][1] > schedule[j][1]:
                schedule[i], schedule[j] = schedule[j], schedule[i]
    # schedule.sort(key = lambda x:x[1])    # 뒤에 것 기준으로 정렬

    # total = 0
    # dfs(0, 1)

    total = 1
    end = schedule[0][1]
    for i in range(N):
        if end <= schedule[i][0]:
            total += 1
            end = schedule[i][1]

    print(f'#{tc + 1} {total}')
