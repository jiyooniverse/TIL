# 13164 최소 비용
import heapq
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # [0, 0]부터 시작해서 [N-1, N-1]로 도착할 때 제일 적은 코스트

    dist = [[98765432] * N for _ in range(N)]
    q = []
    heapq.heappush(q, [0, 0, 0])   # 0,0 지점부터 시작 # cost, row, col
    dist[0][0] = 0

    while q:
        now = heapq.heappop(q)
        now_cost = now[0]
        now_row = now[1]
        now_col = now[2]

        # 연결 되어있는 점 (상하좌우)
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4):
            t_row = now_row + dr[i]
            t_col = now_col + dc[i]
            if 0 <= t_row <= N - 1 and 0 <= t_col <= N - 1:
                # cost 계산
                cost = 1    # 기본 1만큼 들고
                if arr[now_row][now_col] < arr[t_row][t_col]:
                        # 갈 곳이 크면 차이만큼 추가됨
                        cost += arr[t_row][t_col] - arr[now_row][now_col]
                # dist 계산 : 이곳을 거쳐가면 기존에 있던 dist 값보다 작은가
                if dist[t_row][t_col] <= dist[now_row][now_col] + cost:
                    continue
                dist[t_row][t_col] = dist[now_row][now_col] + cost
                heapq.heappush(q, (dist[t_row][t_col], t_row, t_col))


    print(f'#{tc + 1} {dist[N-1][N-1]}')