# 13114 퀵 정렬

def partition(A, l, r):
    # Lomuto partition 알고리즘
    # pivot의 위치 가장 오른쪽값으로(왼쪽도 되고, 가운데 값도 되고 임의 설정)
    x = A[r]

    # i랑 j랑 둘다 lower bound에서 시작해서 upper bound까지(맨 마지막 피봇 위치가면 이 때도 i랑 교환됨) 돌면서
    # j가 pivot보다 작은 값 찾으면 앞으로 넣어주기(i 위치로 넘겨주기)
    i = j = l
    while j <= r:
        # j가 작은 값 찾는 거니까 j기준으로 증가시키기
        if A[j] <= x:
            # 작은 거 찾았으면 i위치로 바꿔주고
            A[i], A[j] = A[j], A[i]
            # i 하나 이동
            i += 1
        # j는 계속 뒤로 간다.
        j += 1

    # pivot 위치 반환해줘야 그거 기준으로 왼쪽 오른쪽 파티션 또 나눠서 이거 반복함
    return i - 1

    # # j는 pivot보다 작은 값 찾기
    # for j in range(l, r):
    #     if A[j] <= x:
    #         i += 1
    #         A[i], A[j] = A[j], A[i]
    #
    # A[i + 1], A[r] = A[r], A[i + 1]
    # return i + 1


def quiksort(A, l, r):

    # lowerbound가 upperbound보다 작을 때까지
    if l < r:
        s = partition(A, l, r)

        # 왼쪽 파티션 다시
        quiksort(A, l, s - 1)
        # 오른쪽 파티션 다시
        quiksort(A, s + 1, r)

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    # 배열 arr의 0부터 N-1 인덱스 정렬(초기 lowerbound, upperbound)
    quiksort(arr, 0, N - 1)

    print(f'#{tc + 1} {arr[N//2]}')

