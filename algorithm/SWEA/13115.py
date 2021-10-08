# 13115 이진 탐색
def binarySearch(n, key):
    low = 0
    high = n - 1

    # 오른쪽-오른쪽, 왼쪽-왼쪽 탈락
    flag_l = flag_r = 0
    while low <= high:
        mid = (low + high) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            if flag_l == 1:
                return -1
            flag_l = 1
            flag_r = 0
            high = mid - 1
        else:
            if flag_r == 1:
                return -1
            flag_r = 1
            flag_l = 0
            low = mid + 1

    return -1

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # A는 정렬된 상태여야 함
    A.sort()

    cnt = 0
    for k in B:
        mid_idx = binarySearch(N, k)
        if mid_idx != -1:
            cnt += 1

    print(f'#{tc + 1} {cnt}')
