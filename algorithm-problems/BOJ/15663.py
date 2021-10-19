# 15663 N과 M (9)
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

arr = [0] * M
check = [0] * N
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
        if check[i] != 0:
            continue
        check[i] = 1
        arr[k] = numbers[i]
        dfs(k + 1)
        check[i] = 0

dfs(0)
