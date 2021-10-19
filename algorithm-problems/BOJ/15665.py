# 15663 N과 M (11)
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
# numbers.sort()
for i in range(N-1, 0, -1):
    for j in range(i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
arr = [0] * M
# check = [0] * N
total_path = set()
# numbers에서 M개 뽑기
def dfs(k):
    if k == M:
        tmp = ''.join(str(s) for s in arr)
        if tmp in total_path:
            return
        total_path.add(tmp)
        print(*arr)

        return

    for i in range(N):
        arr[k] = numbers[i]
        dfs(k + 1)

dfs(0)
