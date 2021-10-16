# BOJ 10163 색종이
# PyPy3로 실행

# N <= 100, 가로 세로 <= 1001
n = int(input())    # 색종이 수

arr = [[0] * 1010 for _ in range(1010)]
count = [0] * 101
for num in range(n):
    # 왼쪽 아래 point, 너비, 높이
    lx, ly, w, h = map(int, input().split())
    for x in range(lx, lx + w):
        for y in range(ly, ly + h):
            # count[arr[x][y]] -= 1
            arr[x][y] = (num + 1)   # num번째 색종이 영역
            # count[num + 1] += 1


# arr 전체를 돌면서 번호에 맞는 영역 개수 세기
for i in range(len(arr[0])):
    for j in range(len(arr[0])):
        count[arr[i][j]] += 1

for j in range(1, n + 1):
    print(count[j])
