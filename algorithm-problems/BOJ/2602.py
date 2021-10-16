# 2602 돌다리 건너기
import sys
strs = list(sys.stdin.readline())
map = [list(sys.stdin.readline()) for _ in range(2)]

starts = []
for j in range(len(map[0])):
    if strs[0] == map[0][j]:
        starts.append([0, j])
    if strs[0] == map[1][j]:
        starts.append([1, j])


def dfs(now, k):
    global cnt
    switch = now[0]^1
    pos = now[1]
    if k == len(strs):
        cnt += 1
        return 1
    if dp[switch][pos][k] != -1:
        return dp[switch][pos][k]
    if len(map[0]) - (pos + 1) < len(strs) - k:
        return 0

    ret = 0
    for i in range(pos + 1, len(map[0])):
        if map[switch][i] == strs[k]:
            ret += dfs([switch, i], k + 1)
    dp[switch][pos][k] = ret
    return ret

cnt = 0
ans = 0
dp = [[[-1] * len(strs) for _ in range(len(map[0]))] for _ in range(2)]
for start in starts:
    ans += dfs(start, 1)

print(ans)
# print(cnt)
