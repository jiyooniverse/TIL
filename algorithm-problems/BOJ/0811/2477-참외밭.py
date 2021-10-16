# 참외밭

# 동, 서, 남, 북: 1, 2, 3, 4
# 6개의 변의 길이

melon = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]

# 방향이 많을 수록 길이가 짧다. (1하고 2비교, 3하고 4비교)
dir_count = [0] * 5 # index: 1부터 4 넣기위해 5개 만들어줌.
for i in range(6):
    dir_count[arr[i][0]] += 1

width_dir = 1
if dir_count[1] > dir_count[2]:
    width_dir = 2

height_dir = 3
if dir_count[3] > dir_count[4]:
    height_dir = 4

# 길이가 긴 width와 height를 찾아준다.
for i in range(len(arr)):
    if arr[i][0] == width_dir:
        width = arr[i][1]
        width_idx = i
    elif arr[i][0] == height_dir:
        height = arr[i][1]
        height_idx = i
small_y = (width_idx + 3) % 6
small_x = (height_idx + 3) % 6

area = (width * height) - (arr[small_x][1] * arr[small_y][1])
result = area * melon

print(result)





