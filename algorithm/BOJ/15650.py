# 15650 N과 M (2)
N, M = map(int, input().split())

# N까지 수중에 M개 선택하기, 중복 없이 선택
# (1, 2) 랑 (2, 1)은 중복 안 됨
arr = [0] * M
check = [0] * N
def dfs(k, s):
    if k == M:
        print(*arr)
        return

    for i in range(s, N):
        if check[i] == 0:
            arr[k] = i + 1
            check[i] = 1
            dfs(k + 1, i)
            check[i] = 0

dfs(0, 0)