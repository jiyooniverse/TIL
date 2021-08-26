# BOJ 1913 달팽이

n = int(input())
find = int(input())

# 아래, 오른쪽, 위, 왼쪽
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

arr = [[0] * n for _ in range(n)]

i = j = d = 0
for num in range(n*n, 0, -1):
    if num == find:
        res = i, j
    arr[i][j] = num
    ni = i + dr[d]
    nj = j + dc[d]

    if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0:
        i = ni
        j = nj
        continue
    else:
        d = (d + 1) % 4
        i += dr[d]
        j += dc[d]

for x in range(n):
    for y in range(n):
        print(arr[x][y], end=" ")
    print()
print(res[0]+1, res[1]+1)
