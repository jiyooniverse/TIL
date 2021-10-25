# BFS(너비 우선 탐색)

- `BFS(Breadth First Search)`는 시작 정점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식이다.
- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비 우선탐색을 진행해야 하므로, <u>선입선출형태의 자료구조인 [큐]()</u>를 활용한다.

> 주로 최소 지점을 거쳐 도착하는 방법에 대해 계산할 때 활용한다. 



- 구현

  ```python
  # BFS
  T = int(input())
  for tc in range(T):
      N, M = map(int, input().split())
      G = [[] for in range(N)]
  	
      for _ in range(M):
  	    a, b = map(int, input().split())
      	G[a].append(b)
  
      q = []	# queue 생성
      q.append(0)	# 시작점 setting
      
      while len(q) != 0:
          now = q.pop(0)
          for next in G[now]:	# now와 인접한 정점들 방문하기 위해 queue에 추가     
              q.append(next)
  ```

  



-----

- 최단 경로 + 경우의 수

  - [숨바꼭질2](https://www.acmicpc.net/problem/12851)

    > visited 확인에 유의하자! 

  ```python
  #12851 숨바꼭질2
  import sys
  from collections import deque
  N, K = map(int, sys.stdin.readline().split())    # 수빈이,동생 위치
  
  # 최단 거리와 경우의 수
  visited = [0] * 100001
  q = deque([[N, 0]])
  visited[N] = 1
  min_dist = 100001
  total = 0
  while q:
      now = q.popleft()
      visited[now[0]] = 1
      if min_dist < now[1]: continue
      if now[0] == K:
          # 동생 위치로 도착
          min_dist = min(min_dist, now[1])
          if min_dist == now[1]:
              total += 1
          continue
  
      # 다음 위치
      for i in range(3):
          if i == 0:
              next = now[0] + 1
          elif i == 1:
              next = now[0] - 1
          else:
              next = now[0] * 2
  
          if 0 <= next <= 100000 and visited[next] == 0:
              q.append([next, now[1] + 1])
  
  print(min_dist)
  print(total)
  ```

  
