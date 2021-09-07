# BOJ 1895 필터
row, col = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(row)]
T = int(input())

dr = [0, 0, 0, 1, 1, 1, 2, 2, 2]
dc = [0, 1, 2, 0, 1, 2, 0, 1, 2]

cnt = 0
temp = []
for i in range(row - 2):
    for j in range(col - 2):
        for k in range(9):
            temp.append(MAP[i+dr[k]][j+dc[k]])
        temp.sort()
        if temp[4] >= T:
            cnt += 1
        temp = []

print(cnt)
