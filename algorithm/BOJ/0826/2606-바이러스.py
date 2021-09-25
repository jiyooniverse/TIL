# BOJ 2060 바이러스
N = int(input())        # node 수
cnt = int(input())      # node 연결 개수
adj = [[0] * N for _ in range(N)]   # 인접 행렬
path = [0] * N
for _ in range(cnt):
    i, j = map(int, input().split())
    adj[i - 1][j - 1] = 1
    adj[j - 1][i - 1] = 1


def dfs(now):
    global result

    for i in range(N):
        if adj[now][i] == 1 and path[i] == 0:   # now와 인접하고 안 지나간 길이면
            path[i] = now + 1
            result += 1
            dfs(i)

result = 0 # 맨처음 시작 할때 더해준 것 빼준다.
path[0] = 1
dfs(0)  # 1에서 시작
print(result)
