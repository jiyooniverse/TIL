# 직사각형

# 다음과 같이 직사각형 좌표 입력 받을 떄
# 왼쪽 아래: x,y  오른쪽 위: p,q
# 두개의 직사각형의 겹치는 유형 출력하기
# a: 직사각형, b: 선분, c: 점, d: 안 겹침

T = 4
for tc in range(T):
    arr = []
    lx1, by1, rx1, ty1, lx2, by2, rx2, ty2 = map(int, input().split())

    width1 = rx1 - lx1
    width2 = rx2 - lx2
    height1 = ty1 - by1
    height2 = ty2 - by2
    # x축 길이 비교 : 왼쪽 끝점과 오른쪽 끝점까지 길이와 사각형 두개 넓이 합과 비교
    lx = lx1; rx = rx2
    if lx1 > lx2:
        lx = lx2
    if rx1 > rx2:
        rx = rx1
    width = rx - lx
    # y축 길이 비교
    by = by1; ty = ty2
    if by1 > by2:
        by = by2
    if ty1 > ty2:
        ty = ty1
    height = ty - by

    if height == (height1 + height2) and width == (width1 + width2):
        result = 'c'    # 점
    elif height == (height1 + height2) and width < (width1 + width2):
        result = 'b'    # 선분
    elif width == (width1 + width2) and height < (height1 + height2):
        result = 'b'  # 선분
    elif width < (width1 + width2) and height < (height1 + height2):
        result = 'a'  # 사각형
    else:
        result = 'd'

    print(result)



