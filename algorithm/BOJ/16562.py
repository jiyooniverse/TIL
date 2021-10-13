# 16562 친구비
N, M, k = map(int, input().split())
arr = list(map(int, input().split()))
group = [i for i in range(N + 1)]


def Find(x):
    if x == group[x]:
        return x
    gx = Find(group[x])
    group[x] = gx
    return gx


def union(x, y):
    gx = Find(x)
    gy = Find(y)
    # 비용이 작은 애를 우두머리로
    if arr[gx - 1] < arr[gy - 1]:
        group[gy] = gx

    else:
        group[gx] = gy


for i in range(M):
    x, y = map(int, input().split())    # x와 y는 친구다
    union(x, y)

# k원이내로 모두 친구가 될 수 있는 최소 비용
check = [0] * (N + 1)
money = 0
for i in range(1, N+1):
    if group[i] != i:
        Find(i)

    if check[group[i]] == 0:
        money += arr[group[i] - 1]

    if money > k:
        break
    check[group[i]] = 1
    check[i] = 1


if money <= k:
    print(money)
else:
    print('Oh no')





