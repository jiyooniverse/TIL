# BOJ 2563 색종이

arr = [[0] * 100 for _ in range(100)]
n = int(input())    # 색종이 수
for i in range(n):
    lx, ly = map(int, input().split())
    for x in range(lx, lx + 10):
        for y in range(ly, ly + 10):
            arr[x][y] = 1

result = 0
for row in range(100):
    for col in range(100):
        result += arr[row][col]
print(result)


