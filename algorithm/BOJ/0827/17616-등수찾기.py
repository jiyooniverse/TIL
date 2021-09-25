# BOJ 17616 등수 찾기
from collections import deque
import sys
N, M, X = map(int, sys.stdin.readline().split())
arr1 = [[] for _ in range(N + 1)]
arr2 = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr1[a].append(b)    # a가 밑으로 깔고가는 학생
    arr2[b].append(a)    # b 위에 있는 학생

check = [0] * (N + 1)
queue = deque()
queue.append(X)
check[X] = 1

cnt = 0
while queue:
    now = queue.popleft()
    cnt += 1
    for i in arr1[now]:
        if check[i] != 0:
            continue
        check[i] = 1
        queue.append(i)
worst = N + 1 - cnt

check = [0] * (N + 1)
queue = deque()
queue.append(X)
check[X] = 1

best = 0
while queue:
    now = queue.popleft()
    best += 1
    for i in arr2[now]:
        if check[i] != 0:
            continue
        check[i] = 1

        queue.append(i)

print(best, worst)
