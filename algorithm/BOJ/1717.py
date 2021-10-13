# 1717 집합의 표현
import sys
n, m = map(int, sys.stdin.readline().split())

def Find(x):
    if x == parents[x]:
        return x

    px = Find(parents[x])
    parents[x] = px
    return px


def Union(x, y):
    px = Find(x)
    py = Find(y)
    parents[py] = px


parents = [i for i in range(n + 1)]
for _ in range(m):
    check, x, y = map(int, sys.stdin.readline().split())
    if check == 0:
        Union(x, y)
    else:
        if Find(x) == Find(y):
            print('YES')
        else:
            print('NO')



