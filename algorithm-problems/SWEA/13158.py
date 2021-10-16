# 13158 연산
from collections import deque

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    check = [0] * 1000001
    q = deque()
    q.append([N, 0])
    check[N] = 1
    ans = 0
    while len(q) != 0:
        now = q.popleft()
        if now[0] == M:
            ans = now[1]
            break
        # 다음 경우의 수
        for i in range(4):
            if i == 0:
                next = now[0] + 1
            elif i == 1:
                next = now[0] - 1
            elif i == 2:
                next = now[0] * 2
            elif i == 3:
                next = now[0] - 10

            if next > 1000000 or next <= 0:
                continue
            if check[next] == 1:
                continue
            q.append([next, now[1] + 1])
            check[next] = 1

    print(f'#{tc + 1} {ans}')
