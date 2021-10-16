# 12921 subtree

T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    tree = [[] for _ in range(E + 2)]
    for i in range(0, len(arr), 2):
        p = arr[i] # 부모
        c = arr[i + 1] # 자식
        tree[p].append(c)
    count = 1

    q = tree[N]
    while len(q):
        s = q.pop()
        count += 1

        while len(tree[s]):
            a = tree[s].pop()
            q.append(a)

    print(f'#{tc + 1} {count}')

## dfs로 풀이
def dfs(now):
    global ans
    ans += 1
    for next in graph[now]:
        dfs(next)

for tc in range(T):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    graph = [[] for _ in range(E + 2)]
    for i in range(E):
        parents = data[i * 2]
        child = data[i * 2 + 1]
        graph[parents].append(child)

        ans = 0
        dfs(N)
        print(f'#{tc + 1} {ans}')