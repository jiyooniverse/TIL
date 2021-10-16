# 1232 사칙연산
T = 10
def dfs(now):
    if now > N:
        return 0
    if len(graph[now]) > 1:
        left = dfs(int(graph[now][1]))
        right = dfs(int(graph[now][2]))
        if graph[now][0] == '+':
            result = left + right
        elif graph[now][0] == '-':
            result = left - right
        elif graph[now][0] == '/':
            result = left / right
        elif graph[now][0] == '*':
            result = left * right
        return int(result)
    else:
        return int(graph[now][0])


for tc in range(T):
    N = int(input())
    graph = [[0] for _ in range(N + 1)]
    for _ in range(N):
        arr = list(input().split())
        if len(arr) == 2:
            graph[int(arr[0])] = [arr[1]]
        else:
            graph[int(arr[0])] = arr[1::]

    print(f'#{tc + 1} {dfs(1)}')
