#SWEA 특별한 정렬
T = int(input())

for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    # arr 내림차순 정리
    for i in range(N-1, 0, -1):
        for j in range(i):  # 큰 수를 앞으로
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    new_arr = [arr[0]]
    for i in range(1, len(arr)//2):
        new_arr += [arr[N-i], arr[i]]
    if N % 2 == 0:
        new_arr += [arr[i+1]]

    arr_str = ' '.join(str(new_arr[i]) for i in range(10))
    print(f'#{test_case + 1} {arr_str}')


# #SWEA 특별한 정렬 (선택 정렬)
# T = int(input())
#
# for test_case in range(T):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     for index in range(N):
#         found = 0   # 찾은 index
#         if index % 2 == 0:  # 짝수 index에는 큰 값을 넣는다.
#             max_value = 0
#             for i in range(index, N):
#                 if max_value < arr[i]:
#                     max_value = arr[i]
#                     found = i
#         else:   # 홀수 index에는 작은 값을 넣는다.
#             min_value = 101
#             for i in range(index, N):
#                 if min_value > arr[i]:
#                     min_value = arr[i]
#                     found = i
#         # 교환
#         arr[index], arr[found] = arr[found], arr[index]
#
#     arr_str = ' '.join(str(arr[i]) for i in range(10))
#     print(f'#{test_case + 1} {arr_str}')