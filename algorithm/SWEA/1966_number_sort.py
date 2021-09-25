# SWEA 숫자 정렬

T = int(input())

for test_case in range(T):
    n = int(input())
    numbers = list(map(int, input().split()))

    for i in range(n-1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    numbers_str = ' '.join(str(num) for num in numbers)
    print(f"#{test_case + 1} {numbers_str}")

# # SWEA 숫자 정렬(2) 선택 정렬로 풀기
#
# T = int(input())
#
# for test_case in range(T):
#     n = int(input())
#     numbers = list(map(int, input().split()))
#
#     for index in range(n):
#         min_index = 0
#         min_value = numbers[index]
#         for i in range(index, n):
#             if min_value >= numbers[i]:
#                 min_value = numbers[i]
#                 min_index = i
#         # 교환
#         numbers[index], numbers[min_index] = numbers[min_index], numbers[index]
#
#     numbers_str = ' '.join(str(num) for num in numbers)
#     print(f"#{test_case + 1} {numbers_str}")