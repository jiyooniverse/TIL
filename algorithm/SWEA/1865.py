# 1865 동철이의 일 분배
def dfs(now, total=1):
    global ans
    if total <= ans:
        return

    if now >= N:
        if total > ans:
            ans = total
        return

    # now번째 사람이 j번째 일 하라고 하기
    for j in range(N):
        if check[j] == 1:
            continue
        # 누가 안 한 일이면 내가 한다.
        check[j] = 1  # j번째 일은 내가 하고
        dfs(now + 1, total * (MAP[now][j] / 100))  # 나 다음 번 친구한테 넘기기
        check[j] = 0  # 원복


T = int(input())
for tc in range(T):
    N = int(input())
    # i번째 사람이 j번째 일을 잘 할 확률
    MAP = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N

    ans = 0
    dfs(0)
    print(f'#{tc + 1} {ans * 100: .6f}')
