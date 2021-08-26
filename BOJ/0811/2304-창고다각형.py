# 창고 다각형

N = int(input())
col_list = [0] * 1010
start = 1000
end = 0

for _ in range(N):
    L, H = map(int, input().split())
    col_list[L] = H

    if L < start:
        start = L
    if L > end:
        end = L

max_height = max(col_list)
max_index = col_list.index(max_height)
height = 0
result = 0
for i in range(start, max_index + 1):
    if col_list[i] > height:
        height = col_list[i]

    result += height

height = 0
for i in range(end, max_index, -1):
    if col_list[i] > height:
        height = col_list[i]

    result += height

print(result)
