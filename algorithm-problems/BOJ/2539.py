# 2539 모자이크
R, C = map(int, input().split())
num = int(input().split())  # 색종이 장수
color = int(input().split())    # 잘 못 칠해진 칸수

paper = [list(map(int, input().split())) for _ in range(color)] # 잘 못 칠한 칸 r,c

# paper를 다 가릴 수 있는 가장 작은 색종이 크기
