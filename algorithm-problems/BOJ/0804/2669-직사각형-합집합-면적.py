# 직사각형 네개의 합집합의 면적 구하기

# 100*100 빈 리스트 생성
total = []

for i in range(100):
    total.append([0]*100)

# input 받기
for _ in range(4):
    rect = list(map(int, input().split()))
    for x in range(rect[0], rect[2]):
        for y in range(rect[1], rect[3]):
            total[x][y] = 1 
                
result = 0
for i in range(100):
    result += sum(total[i])

print(result)