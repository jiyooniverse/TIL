# BOJ 9934 완전 이진 트리
# 중위 탐색 결과를 보고 입력 트리 구하기
def inorder(now, depth):
    global cnt
    global K
    if depth > K:
        return
    inorder(2*now, depth + 1)
    G[now] = arr[cnt]
    cnt += 1
    inorder(2 * now + 1, depth + 1)


K = int(input())    # level
arr = list(map(int, input().split()))
G = [0] * (1 << K)    # 노드 개수는 2^K - 1, 0번째 인덱스 사용 안 할 거므로 + 1
cnt = 0
inorder(1, 1)  # 1번 노드부터 시작

for i in range(K):
    for j in range(1 << i):
        print(G[2**i + j], end=" ")
    print("")
