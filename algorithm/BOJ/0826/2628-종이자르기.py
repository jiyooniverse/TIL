# BOJ 2628 종이자르기
M, N = map(int, input().split())
cnt = int(input())
row = [0]
col = [0]
for i in range(cnt):
    d, num = map(int, input().split())
    if d == 0:  # 가로 방향으로 자를 거임
        row.append(num)
    else:
        col.append(num)

row += [N]
col += [M]
row.sort()
col.sort()
max_rl = max_cl = 0
for j in range(len(row) - 1):
    temp = row[j + 1] - row[j]
    if temp > max_rl:
        max_rl = temp
for k in range(len(col) - 1):
    temp = col[k + 1] - col[k]
    if temp > max_cl:
        max_cl = temp
print(max_rl * max_cl)


