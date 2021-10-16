# 전기 버스

T = int(input())
for tc in range(T):
    k, n, m = map(int, input().split())
    chargers = list(map(int, input().split()))
    # 1 3 5 7 9 위치값 저장
    # -> li[index] => index  위치
    li = [0] * n
    for i in range(len(chargers)):
        li[chargers[i]] = 1

    now = 0
    cnt = 0
    while now + k < n:
        # next = now
        for i in range(now + 1, now + k + 1):
            # i -> now + 1 ~ now + k
            if li[i] == 1:
                next = i
        if next == now:
            break
        now = next
        cnt += 1
    if now + k >= n:
        print("#{} {}".format(tc + 1, cnt))
    else:
        print("#{} {}".format(tc + 1, 0))



# def next_stop(curr, count=0):
#     global min_count
#     if curr + 1 <= N <= curr + K:
#         if count < min_count:
#             min_count = count
#
#     for _next in range(curr + 1, curr + K + 1):
#         if _next in bus_stop:
#             next_stop(_next, count + 1)
#     return 0
#
# T = int(input())
# for test_case in range(T):
#     # 충전시 가능 거리, 종점, 충전기 설치 개수
#     K, N, M = map(int, input().split())
#     min_count = M + 1
#     # 충전기 설치 정류장
#     bus_stop = list(map(int, input().split()))
#     # 최소한 몇번 충전해야 종점에 도착할 수 있는가
#     # 최대 갈 수 있는 거리 : K
#     next_stop(0)
#     if min_count > M:
#         min_count = 0
#     print(f'#{test_case + 1} {min_count}')
#
#