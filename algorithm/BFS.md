# BFS(너비 우선 탐색)









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

  
