# BOJ 22341 사각형 면적
import sys
N, C = map(int, sys.stdin.readline().split())
A = B = N
for _ in range(C):
    row, col = map(int, sys.stdin.readline().split())
    if col >= A or row >= B:
        continue

    if col * B <= row * A:
        B = row
    else:
        A = col

print(A*B)