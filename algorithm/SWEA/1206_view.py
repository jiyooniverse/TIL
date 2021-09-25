# View

for test_case in range(10):
    width = int(input())
    building_height = list(map(int, input().split()))

    result = 0
    for i in range(2, len(building_height) - 2):
        # i번째 빌딩 앞 2개 뒤 2개 층수 비교해서 가장 작은 수(음수이면 0)
        min_view = 255  # 빌딩의 최대 높이
        for j in range(-2, 3):
            if j == 0:
                continue
            view_count = building_height[i] - building_height[i + j]
            if view_count < min_view:
                min_view = view_count
        if min_view < 0:
            min_view = 0
        result += min_view

    print(f'#{test_case + 1} {result}')
