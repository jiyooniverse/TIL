# 3124 최소 스패닝 트리
# 1. Kruskal's algorithm
# def Find(x):
#     if parents[x] == x:
#         return x
#
#     px = Find(parents[x])
#     parents[x] = px
#     return px
#
#
# def Union(x, y):
#     px = Find(x)
#     py = Find(y)
#     parents[py] = px
#
# T = int(input())
# for tc in range(T):
#     V, E = map(int, input().split())
#     parents = [i for i in range(V + 1)]
#     edges = []
#     for _ in range(E):
#         a, b, cost = map(int, input().split())
#         edges.append((cost, a, b))
#     edges.sort()    # cost순으로 정렬
#     total_cost = 0
#
#     for i in range(E):
#         cost, f, t = edges[i]
#         if Find(f) == Find(t):
#             # 연결되어 있으면 넘어가
#             continue
#         Union(f, t)
#         total_cost += cost
#
#     print(f'#{tc + 1} {total_cost}')




#############
# 2. Prim's algorithm (heap사용)
import heapq
T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    Graph = [[] for _ in range(V + 1)]
    total_cost = 0
    # 인접 리스트
    for _ in range(E):
        a, b, cost = map(int, input().split())
        Graph[a].append((cost, b))
        Graph[b].append((cost, a))  # 무방향이니까 양쪽 다 채워줘

    hq = []     # 힙으로. 힙이 알아서 정렬해준다.
    visited = [0] * (V + 1)     # Kruskal's 알고리즘에서 같은 부모인지 비교했던 것 처럼

    # 임의의 점 f에서 시작 (f = 1으로 해봤다.)
    for cost, t in Graph[1]:
        # 일단 시작점에서 연결된 애들 싹다 넣어
        # hp라는 힙에다가 (cost, to) 튜플 넣는다. 이렇게 넣으면 cost순으로 알아서 정렬해줌
        heapq.heappush(hq, (cost, t))
    visited[1] = 1

    while hq:
        # 가장 작은 cost 꺼내서, 시작점에서 한거 반복
        now = heapq.heappop(hq)    # 힙이여서 젤 작은거 알아서 뽑아줌
        now_cost = now[0]
        now_t = now[1]  # 위에 0처럼 이제 얘부터 시작하는 거
        # 근데, 사이클을 만들면 안 됨 (visited로 판별)
        if visited[now_t] == 1:
            continue
        total_cost += now_cost
        visited[now_t] = 1  # Union해서 같은 그룹 중복 안 되게 하는 거랑 비슷
        # 얘는 이제 now_t에서 갈 다음 애들 찾아서 힙에 넣어줘야함
        for cost, t in Graph[now_t]:
            heapq.heappush(hq, (cost, t))

    print(f'#{tc + 1} {total_cost}')