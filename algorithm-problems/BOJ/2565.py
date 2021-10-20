# 2565 전깃줄
import sys
N = int(sys.stdin.readline().rstrip())    # 전기줄 개수
edges = []
for _ in range(N):
    f, t = map(int, sys.stdin.readline().split())
    edges.append([f, t])

# 출발점에서 오름차순하고 도착점 숫자 배열 중에 증가로만 이루어진 가장 긴 길이
edges.sort()


def dfs(now, cnt=1):
    global max_cnt
    max_cnt = max(max_cnt, cnt)
    if (N-1-now) + cnt <= max_cnt:
        return

    for i in range(now+1, N):
        if edges[i][1] > edges[now][1]:
            dfs(i, cnt + 1)


max_cnt = 0
for i in range(N):
    dfs(i)
print(N - max_cnt)

# 다른 답안 # dp활용
# import sys
# input = sys.stdin.readline
# 
# cnt = int(input())
# line = [list(map(int, input().split())) for _ in range(cnt)]
# 
# line.sort(key= lambda x:x[0])
# 
# dp = [1 for _ in range(cnt)]
# for i in range(cnt):
#     for j in range(i):
#         if line[i][1] > line[j][1]:
#             dp[i] = max(dp[i], dp[j]+1)
# 
# print(cnt-max(dp))