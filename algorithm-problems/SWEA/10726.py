# 10726 이진수 표현
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    # M의 이진수 표현 마지막 N비트가 모두 1이면 ON

    cnt = 0
    for i in range(N):
        if M & (1 << i):
            cnt += 1

    if cnt == N:
        print(f'#{tc + 1} ON')
    else:
        print(f'#{tc + 1} OFF')