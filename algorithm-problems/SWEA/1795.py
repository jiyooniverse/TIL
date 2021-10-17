# 1795 인수의 생일 파티
# 1번부터 N번까지 집, X번집으로 가기 위한 최소 시간
from collections import deque

T = int(input())
for tc in range(T):
    N, M, H = map(int, input().split())

    edges = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        edges[x].append([c, y])  # x에서 y로 가는데 c만큼 걸림 # 단방향

    dist = [[987654321] * (N + 1) for _ in range(N + 1)]    # from-to
    max_dist = 0
    for i in range(1, N+1):

        # q 생성 및 초기화
        q = deque()
        q.append(i)
        dist[i][i] = 0  # 시작 위치 cost 0으로 초기화

        # 전체 집 다 돌때 까지
        while q:
            now = q.popleft()

            # 다음 집 탐색
            for cost, to in edges[now]:
                # 갈 수 있는 집에 이미 더 좋은 선택지가 있으면 됐고,
                # 아니면 지금 집 거쳐서 가는 시간 넣기
                if dist[i][to] <= dist[i][now] + cost:
                    continue
                dist[i][to] = dist[i][now] + cost
                if i != H and to == H:
                    continue
                q.append(to)

    for i in range(1, N+1):
        max_dist = max(max_dist, dist[H][i] + dist[i][H])

    print(f'#{tc + 1} {max_dist}')


