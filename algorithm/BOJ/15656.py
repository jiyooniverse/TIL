# 15656 N과 M (7)
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# numbers 오름차순 sorting
for i in range(N-1, 0, -1):
    for j in range(i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
arr_set = set()
arr = [0] * M
check = [0] * N
def dfs(k):
    if k == M:
        # print(*arr)
        arr_set.add(arr)
        return

    for ii in range(N):
        # numbers 순서랑 check 순서랑 같다.
        if check[ii] == 0:
            arr[k] = numbers[ii]
            check[ii] = 1
            dfs(k + 1)
            check[ii] = 0


dfs(0)
print(*arr_set)
