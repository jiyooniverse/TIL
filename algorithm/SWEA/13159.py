# 13159 그룹 나누기
def Find(x):
    if x == parents[x]:
        return x

    px = Find(parents[x])
    parents[x] = px     # path-compression
    return px

def Union(x, y):
    px = Find(x)
    py = Find(y)
    parents[py] = px


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    parents = [i for i in range(N + 1)]
    for i in range(M):  # m쌍의 번호가 주어진다
        x, y = nums[2*i], nums[2*i+1]
        Union(x, y)

    for i in range(N + 1):
        Find(i)

    print(f'#{tc + 1} {len(set(parents))-1}')   # 0빼기