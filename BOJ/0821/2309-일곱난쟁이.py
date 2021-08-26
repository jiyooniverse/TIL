# BOJ 2309 일곱 난쟁이

height = []
for _ in range(9):
    height.append(int(input()))

# bubble sorting
for i in range(len(height) - 1, 0, -1):
    for j in range(i):
        if height[j] > height[j + 1]:
            height[j], height[j + 1] = height[j + 1], height[j]

# 9개중에서 7개 선택해서
flag = 0
for i in range(1<<len(height)):
    if flag != 0:
        break
    candi = []
    for j in range(len(height)):
        if 1<<j & i != 0:   # 부분집합중
            candi.append(height[j])
        if len(candi) == 7 and sum(candi) == 100:   # 7개만 선택되고 합이 100일때 완성
            flag = 1
            break

for k in range(7):
    print(candi[k])