# 12937 노드의 합
T = int(input())

def dfs(now):
    if now > N:
        return
    dfs(now * 2)
    dfs(now * 2 + 1)
    if graph[now] == 0:
        graph[now] = graph[now * 2]
        if now * 2 + 1 <= N:
            graph[now] += graph[now * 2 + 1]
    # print(graph[now], now)



for tc in range(T):
    N, M, L = map(int, input().split())
    graph = [0] * (N + 1)
    for _ in range(M):
        node, num = map(int, input().split())
        graph[node] = num
    res = 0
    dfs(1)

    print(f'#{tc + 1} {graph[L]}')


# def postorder(now):
#     # 현재 now번째
#     global N
#     if now > N:
#         return 0
#     if node[now] != 0:
#         return node[now]
#         # 계산하거나 알고 있는 값이면 그냥 가져와라(다시 계산하지 말라)
#         # Dynamic Programming <- 가면서 계산하기 보다는 뒤에껄 계산해와서 내껄 계산하는 방식
#     left = postorder(now * 2) # 왼쪽
#     right = postorder(now * 2 + 1) # 오른쪽
#     node[now] = left + right
#     return node[now]
#
# T = int(input())
# for tc in range(T):
#     N, M, L = map(int, input().split())
#     node = [0] * (N + 1) # N번까지 있도록 1차원 배열 구성
#     for i in range(M):
#         num, value = map(int, input().split())
#         node[num] = value # leaf node setting
#     postorder(1) # 1번 node부터 시작해서 아래로 계산해와라!
#     print(f"#{tc + 1} {node[L]}")
#     # 완전 이진 트리