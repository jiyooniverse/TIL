# 1952 수영장
def dfs(now, cost):
    global min_cost
    if now > 11:
        if min_cost > cost:
            min_cost = cost
        return

    dfs(now + 1, cost + d * plan[now])  # 1일
    dfs(now + 1, cost + m1)    # 1달
    # dfs(now + 1, cost + min(m1, d))
    dfs(now + 3, cost + m3)  # 3달


T = int(input())
for tc in range(T):
    d, m1, m3, y = map(int, input().split())
    plan = list(map(int, input().split()))

    min_cost = y
    dfs(0, 0)
    print(f'{tc + 1} {min_cost}')



    # #############DP############
    # month = plan
    # dp = [0] * 13
    # dp[1] = min(m1, month[1] * d)
    # dp[2] = dp[1] + min(m1, month[2] * d)
    #
    # for i in range(3, 13):
    #     dp[i] = min(dp[i-3] + m3, dp[i-1] + m1, dp[i-1] + month[i] * d)
    #
    # min_cost = min(dp[12], y)

