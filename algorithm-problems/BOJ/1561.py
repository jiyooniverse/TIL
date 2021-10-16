# 1561 N과 M (3)
N, M = map(int, input().split())

arr = [0] * M

def dfs(k):
    if k == M:
        arr_str = ' '.join(str(x) for x in arr)
        print(arr_str)
        return

    for i in range(N):
        arr[k] = i + 1
        dfs(k + 1)

dfs(0)