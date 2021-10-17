# 1251 하나로
# N개의 섬을 부담금 최소로 모두 연결
import heapq
T = int(input())
for tc in range(T):
    N = int(input())    # 섬의 개수
    X = list(map(int, input().split())) # 섬들의 x 좌표
    Y = list(map(int, input().split())) # 섬들의 y 좌표
    E = float(input())    # 세율  0 <= E <= 1

    # a섬과 b섬 길이 = L 이면 부담금은 L*L*E
    edges = [[] for _ in range(N)]
    L = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # i 번째 섬과 j번째 섬 길이 계산
            if i == j: continue
            xl = X[i] - X[j]
            yl = Y[i] - Y[j]
            # L[i][j] = L[j][i] = (xl*xl + yl*yl)**0.5
            cost = (xl*xl + yl*yl)
            edges[i].append([cost, j])
            # edges[j].append([cost, i])


    # E는 모든 거리에 다 곱해지므로 거리로 최소 값 찾은 다음에 마지막 답에 E 곱해주기
    # 1. q생성 및 초기화
    q = []
    heapq.heappush(q, [0, 0])
    # 2. 각 섬 방문 여부 표시
    dist = [9876543211] * N
    dist[0] = 0
    visited = [False] * N
    ans = 0
    while q:
        now = heapq.heappop(q)
        now_cost = now[0]
        now_num = now[1]

        if visited[now_num]:
            continue
        visited[now_num] = True
        ans += now_cost

        for c, t in edges[now_num]:
            if visited[t]:
                continue
            heapq.heappush(q, [c, t])

    print(f'#{tc + 1} {round(ans*E)}')




