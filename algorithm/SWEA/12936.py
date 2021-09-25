# 12936 이진힙
import heapq
T = int(input())

for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))

    data = []
    for number in numbers:
        heapq.heappush(data, number)

    data.insert(0, 0)
    index = len(data) - 1
    res = 0
    while index // 2:
        index //= 2
        res += data[index]

    print(f'#{tc + 1} {res}')

# 다른 사람 풀이 1
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     tree = [0] * (N+1)
#     cnt = 1
#     for i in nums:
#         now = cnt
#         tree[now] = i
#         while now != 1 and tree[now//2] > tree[now]:
#             tree[now//2], tree[now] = tree[now], tree[now//2]
#             now //= 2
#         cnt += 1
#     N //= 2
#     result = 0
#     while N >= 1:
#         result += tree[N]
#         N //= 2
#     print(f'#{tc} {result}')


############
# 다른 사람 풀이 2
# def insert(value): # heap 구조로 node에 value를 추가
#     # 1. 일단 맨 뒤에 data 추가
#     node.append(value)
#     pos = len(node) - 1
#     # 2. 올바른 위치 될 때까지 부모랑 swap
#     while pos != 0 and node[pos // 2] > node[pos]:
#         node[pos//2], node[pos] = node[pos], node[pos//2]
#         pos //= 2
