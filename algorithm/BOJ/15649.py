# 15649 N과 M (1)

N, M = map(int, input().split())

arr = [0] * M
check = [0] * N
def dfs(k):
    if k == M:
        arr_str = ' '.join(str(x) for x in arr)
        print(arr_str)
        return

    for i in range(N):  # 사전순
        if check[i] == 0:
            arr[k] = i + 1
            check[i] = 1
            dfs(k + 1)
            check[i] = 0

dfs(0)
