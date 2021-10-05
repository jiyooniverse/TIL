# 15654 N과 M (5)

# N개의 자연수 nums들 중에 M개를 선택해서 순열 만들기
N, M = map(int, input().split())
nums = list(map(int, input().split()))

# nums 오름차순으로 sorting
for j in range(N - 1, 0, -1):
    for i in range(j):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

arr = [0] * M
check = [0] * 10001
def dfs(k):
    if k == M:
        print(*arr)
        return

    for j in range(N):
        if check[nums[j]] == 0:
            check[nums[j]] = 1
            arr[k] = nums[j]
            dfs(k + 1)
            check[nums[j]] = 0

dfs(0)