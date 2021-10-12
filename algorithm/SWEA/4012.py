# 4012 요리사

# 1. 재료 나누기
def select(now=0, path=[]):
    if len(path) == N//2:
        pick_a.append(path)
        pick_b.append(list(set(range(N)) - set(path)))
        return

    for i in range(now, N):
        select(i + 1, path + [i])


# 2. 재료 합 구하기
def dfs(path_a, path_b):
    sum_a = sum_b = 0
    for i in range(len(path_a)-1):
        for j in range(i + 1, len(path_a)):
            a1 = path_a[i]
            a2 = path_a[j]
            sum_a += arr[a1][a2]
            sum_a += arr[a2][a1]

            b1 = path_b[i]
            b2 = path_b[j]
            sum_b += arr[b1][b2]
            sum_b += arr[b2][b1]
    return abs(sum_a - sum_b)

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 재료 나누는 모든 경우 구하기
    pick_a = []
    pick_b = []
    select()

    #
    min_ans = 987654321
    for i in range(len(pick_a)):
        ans = dfs(pick_a[i], pick_b[i])
        if ans < min_ans:
            min_ans = ans

    print(f'#{tc + 1} {min_ans}')
