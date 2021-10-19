# DFS(깊이 우선 탐색)

- `DFS(Depth First Search)`는 시작 정점에서 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색하다가 더 이상 갈 수 있는 곳이 없다면 가장 마지막 갈림길로 다시 돌아가 다른 방향의 정점으로 탐색하는 것을 반복하며 모든 정점을 방문하는 방법이다.
- 가장 마지막으로 들렸던 갈림길로 되돌아가는 구조로 <u>후입선출 구조의 [스택]()</u>을 사용한다.

> 주로 모든 방법을 다 해봐야하는 상황에 사용한다.



- 구현

  - 반복문

    ```python
    def dfs1(s, V):
        visited = [0] * (V+1)
        stack = []
        i = s	# 현재 방문한 점
        visited[i] = 1
        print(node[i])
        while i != 0:
            for w in range(1, V+1):
                if adj[i][w] == 1 and visited[w] == 0:
                    stack.append(i)
                    i = w	# 새 방문지
                    visited[w] = 1
                    print(node[i])
                    break
             else:	# 다음 정점 없을 때
                if stack:
                    i = stack.pop(-1)	
                else:
                    i = 0	# stack 끝
          return
    ```
  
  - 반복문
  
    ```python
    visited = [0] * 8
    prev = [0] * 8		# 누구를 통해서 왔는가
    #counts = [0] * 8	# 얼마만에 왔는가
    visited = [0] * 8	# 방문 표시이지만 count기능도 가능
    def dfs2(now):
        # 기저 조건
        if now > 8:
            return
        
        # now에서 갈 수 있는 다음 노드들 탐색
    
        # 1. 그래프 이용 시
        # for next in graph[now]:
        #	if visited[next] == 0:	#	next가 다음에 갈 수 있는 노드
        
        # 2. 인접행렬 이용시
        for i in range(1, 8):
            if adj[now][i] == 1 and visited[i] == 0:	
                next = i
                visited[next] = 1	# next로 움직인다.
                # visited[next] = visited[now] + 1	# count 세는 것
                prev[next] = now
                dfs2(next)         
      
    
    visited[1] = 1
    dfs2(1)
    ```
    
    



- DFS 뿌시기 :[ BOJ - N과 M문제 시리즈](https://www.acmicpc.net/problemset?search=N%EA%B3%BC+M)
  - [풀이 정리](https://github.com/jiyooniverse/TIL/blob/master/algorithm/%EC%88%9C%EC%97%B4-%EC%A1%B0%ED%95%A9.md)

