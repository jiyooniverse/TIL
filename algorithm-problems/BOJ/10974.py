# 10974 모든 순열

N = int(input())

arr = [0] * N
check = [0] * N
def dfs(k):
    if k == N:
        arr_str = ' '.join(str(x) for x in arr)
        print(arr_str)
        return

    for i in range(N):
        if check[i] == 0:
            arr[k] = i + 1
            check[i] = 1
            dfs(k + 1)
            check[i] = 0

dfs(0)
