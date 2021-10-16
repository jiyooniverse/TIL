# BOJ 1987 알파벳
import sys

r, c = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().rstrip() for _ in range(r)]
visited = [0] * 256
def dfs(row, col, cnt):
    #
    global  max_cnt
    if cnt > max_cnt:
        max_cnt = cnt
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        next_row = row + dr[i]
        next_col = col + dc[i]
        if 0 <= next_col < c and 0 <= next_row < r \
                and visited[ord(arr[next_row][next_col])] == 0:
            visited[ord(arr[next_row][next_col])] = 1
            dfs(next_row, next_col, cnt + 1)
            visited[ord(arr[next_row][next_col])] = 0

max_cnt = 0
visited[ord(arr[0][0])] = 1
dfs(0, 0, 1)
print(max_cnt)
