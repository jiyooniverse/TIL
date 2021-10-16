# 최소 신장 트리(MST, Minimum Spanning Tree)

- **신장 트리(Spanning Tree)**
  - n개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리
  - **모든 정점들이 연결어 있으며 사이클이 허용되지 않음**
- **최소 신장 트리(Minimum Spanning Tree)**
  - 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치 합이 최소인 신장 트리
  - **그래프에서 최소 비용 문제**에 적용 가능
    - 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리
    - 두 정점 사이의 최소 비용의 경로 찾기



### 구현

#### 1. Kruskal Algorithm

- `간선` 하나씩 선택해서 MST 만드는 알고리즘

  1. 모든 간선을 가중치에 따라 오름차순으로 정렬

  2. 가중치가 가장 작은 간선부터 선택하며 트리 증가

     - **사이클 존재 시** 다음 우선 순위의 간선 선택(사이클 없게 선택해야함)

       > Disjoint Set(서로소 집합)이나 Union-Find 알고리즘 이용하여 사이클 제외

  3. `N-1`개의 간선 선택될 때 까지 반복

  

  ```python
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
      
  n, m = map(int, input().split())	# n개의 정점, m개의 간선    
  parents = [i for i in range(n + 1)]	# make-set
  edges = []
  for i in range(m):
      f, t, cost = map(int, input().split())
      edges.append((cost, f, t))	# from-to 정점과 간선 가중치 입력 받음
  edges.sort()	# 가중치에 따라 오름차순 정렬
  total_cost = 0
  for cost, f, t in edges:
      # 사이클 제외하도록 같은 그룹이면 제외
      if Find(f) == Find(t):
          continue
      Union(f, t)			# f와 t 연결하는 간선 선택 
      total_cost += cost	# 해당 간선 cost 추가
  ```



#### 2. Prim Algorithm

- 하나의 `정점`에서 연결된 간선들 중에 하나씩 선택하면서 MST 만드는 알고리즘

  1. 임의의 정점 하나 선택

  2. 선택한 정점과 인접하는 정점들 중 최소 비용의 간선이 존재하는 정점 선택

     > 자료구조 힙(heap) 사용

  3. 모든 정점이 선택될 때 까지 반복

  

  ```python
  import heapq
  
  n, m = map(int, input().split())
  Graph = [[] for _ in range(n + 1)]
  total_cost = 0
  # 인접리스트 생성
  for i in range(m):
      f, t, cost = map(int, input().split())
      Graph[f].append((cost, t))
      Graph[t].append((cost, f))	# 무방향이기 때문에 양쪽 정점에 모두 추가
      
  hq = []
  visited = [False] * (n + 1)	# 같은 그룹에 포함시켰는지 확인
  
  # 임의의 정점(0)을 시작점으로 세팅 후 시작점에 연결된 선 모두 heap에 추가
  visited[0] = True
  for cost, t in Graph[0]:
      heapq.heappush(hq, (cost, t))	# 힙에서 cost 오름차순 정렬
      
  while hq:
      # 제일 최소 비용으로 연결된 정점 선택
      now = heapq.heappop(hq)
      now_cost = now[0]
      now_t = now[1]
      
      # 정점 사이클 확인
      if visited[now_t] == True:
          continue
      # 사이클 생성 안 되면 이 정점 선택
      visited[now_t] = True
      total_cost += now_cost
      # 이 정점에서 갈 수 있는 연결된 선 모두 추가(시작점에서 세팅했던 것 반복)
      for cost, t in Graph[now_t]:
          heapq.heappush(hq, (cost, t))
  ```

  