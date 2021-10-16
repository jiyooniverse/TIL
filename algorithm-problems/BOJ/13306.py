# 13306 트리
import sys
sys.setrecursionlimit(200000)
def Find(x):
    if parents[x] == x:
        return x
    px = Find(parents[x])
    parents[x] = px
    return px

def Union(x, y):
    px = Find(x)
    py = Find(y)
    parents[py] = px    # py 밑에 있는 애들 다 px 밑으로 들어가

N, Q = map(int, sys.stdin.readline().split())
_parents = [i for i in range(N + 1)]
parents = [i for i in range(N + 1)]
for i in range(1, N):   # 1번은 무조건 루트이다.
    _parents[i + 1] = int(sys.stdin.readline())

# 거꾸로 실행하기 - union
ans = [0] * Q
query = [list(map(int, sys.stdin.readline().split())) for _ in range(Q+N-1)]
i = 0
for x in query[::-1]:
    if x[0] == 0:
        # parents[x[1]] = x[1]  # b의 부모 제거
        parents[x[1]] = _parents[x[1]]  # Union(x[1], _parents[x[1]])

    elif x[0] == 1:
        # x[1]하고 x[2]하고 연결되어있는지 질의
        if Find(x[1]) == Find(x[2]):
            ans[i] = 1   # print('YES')
        else:
            ans[i] = 0   # print('NO')
        i += 1


for a in ans[::-1]:
    if a == 1:
        print('YES')
    else:
        print('NO')



