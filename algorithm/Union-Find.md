# Union-Find

**서로소 집합**(disjoint-set) 자료 구조에서 사용 가능한 연산

- `Find` : 원소의 조상 찾기 (내가 어떠한 그룹인가?)
- `Union` : 두 개의 그룹을 같은 그룹으로 묶는 연산 (한 쪽의 조상을 다른 쪽 조상 밑으로 넣는다.)
- `MakeSet` : 한 원소만을 가지는 그룹 생성



### **구현**

- **MakeSet** 

  ```python
  parents = [i for i in range(N)]	# make_set
  ```

- **Find**

  ```python
  def Find(x):
      if x == parents[x]:
          return x
      px = Find(parents[x])
      parents[x] = px		# path-compression
      return px
  ```

- **Union**

  ```python
  def Union(x, y):
      px = Find(x)
      py = Find(y)
      if px == py:
          return
      parents[py] = px
      cnt[px] += cnt[py]	# root에 원소 개수 몰아주기
      cnt[py] = 0
      
  cnt = [1] * (N + 1)	# 각 그룹의 원소 개수
  ```
