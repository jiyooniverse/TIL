# 17619 개구리 점프
# Union-Find
import sys
# sys.stdin = open('input.txt', 'r')
N, Q = map(int, sys.stdin.readline().split())
parents = [i for i in range(N + 1)]

def Find(x):
    if parents[x] == x:
        return x

    px = Find(parents[x])
    parents[x] = px
    return px


def Union(x, y):
    px = Find(x)
    py = Find(y)
    parents[py] = px


wood = [[] for _ in range(N)]
for i in range(N):
    x1, x2, y = map(int, sys.stdin.readline().split())
    wood[i] = [x1, x2, i + 1]

wood.sort()
left = wood[0][0]
right = wood[0][1]
for i in range(N - 1):
    if left <= wood[i+1][0] <= right:
        Union(wood[i][2], wood[i+1][2])
        right = max(right, wood[i+1][1])
    else:
        left = wood[i+1][0]
        right = wood[i+1][1]

for q in range(Q):
    w1, w2 = map(int, sys.stdin.readline().split())

    if Find(w1) == Find(w2):
        print(1)
    else:
        print(0)
