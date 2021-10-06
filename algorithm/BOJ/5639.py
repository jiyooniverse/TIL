# 5639 이진 검색 트리
import sys
sys.setrecursionlimit(100000)

def postorder(now):
    global count2
    if now > len(inorder):
        return
    postorder(now * 2)
    postorder(now * 2 + 1)
    print(graph[now])


def dfs(now):
    global count
    if now > len(inorder) or inorder[count] > inorder[count - 1]:
        return

    graph[now] = inorder[count]
    count += 1
    dfs(now * 2)
    dfs(now * 2 + 1)


inorder = list(map(int, sys.stdin.read().split()))
graph = [0] * (len(inorder) + 1)
count = 0
dfs(1)

postorder(1)



####################
# import sys
#
# sys.setrecursionlimit(100000)
#
# data = list(map(int, sys.stdin.read().split()))     # split : 띄어쓰기, \t, \n 모든 공백 기준
#
# def dfs(s, e):
#     if s > e:
#         return
#     # s~e구간 sub tree 순회
#     now = data[s]   # 현재 sub tree의 root
#
#     # left 구간과 right 구간 나뉘는 지점 찾기
#     mid = e
#     while now < data[mid]:
#         mid -= 1
#
#     dfs(s + 1, mid)     # 왼쪽
#     dfs(mid + 1, e)     # 오른쪽
#
#     print(now)  # 후위 순회 출력
#
#
# dfs(0, len(data) - 1)
