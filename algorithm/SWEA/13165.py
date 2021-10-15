# 13165 최소 이동 거리
import heapq
T = int(input())
for tc in range(T):
    N, E = map(int, input().split())
    edges = [[] for _ in range(E)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        edges[s].append((w, e))     # 일방 통행

    dist = [98765432] * (N + 1)
    q = []
    heapq.heappush(q, [0, 0])   # 0번 지점부터 시작
    dist[0] = 0

    while q:
        now = heapq.heappop(q)
        now_cost =now[0]
        now_t = now[1]

        for cost, t in edges[now_t]:
            if dist[t] <= dist[now_t] + cost:
                continue
            dist[t] = dist[now_t] + cost
            heapq.heappush(q, (cost, t))

    print(f'#{tc + 1} {dist[N]}')
