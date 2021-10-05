# 15657 N과 M (8)
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# numbers 오름차순 sorting
for i in range(N-1, 0, -1):
    for j in range(i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

arr = [0] * M
def dfs(k, s):
    if k == M:
        print(*arr)
        return

    for ii in range(s, N):
        arr[k] = numbers[ii]
        dfs(k + 1, ii)

dfs(0, 0)
