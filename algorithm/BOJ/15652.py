# 15652 N과 M (4)
N, M = map(int, input().split())

arr = [0] * M
# [1, 2] 와 [2, 1]가 중복되면 안 된다
# k번째 넣을 숫자는 s보다 크거나 같은 수
def dfs(k, s):
    if k == M:
        arr_str = ' '.join(str(x) for x in arr)
        print(arr_str)
        return
    
    for i in range(s, N + 1):
        arr[k] = i
        dfs(k + 1, i)

dfs(0, 1)