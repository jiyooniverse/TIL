# count sort로 풀기
for test_case in range(10):
    dump_count = int(input())
    box_list = list(map(int, input().split()))

    box_count = [0] * 101  # 박스 최대 높이 100
    box_count[0] = 100 - len(box_list)
    for i in range(len(box_list)):
        box_count[box_list[i]] += 1

    count = 0
    max_index = 100 # 최대 박스 높이
    min_index = 0   # 최저 박스 높이
    while box_count[max_index] == 0:
        max_index -= 1
    while box_count[min_index] == 0:
        min_index += 1

    while count < dump_count:
        # 최대 박스 높이에 박스 없으면 작은쪽에 있나 보기
        if box_count[max_index] == 0:
            max_index -= 1
        # 최대 박스 높이에 박스 있으면 박스하나 빼서
        box_count[max_index] -= 1
        box_count[max_index - 1] += 1
        # 제일 낮은 높이에 박스 넣어준다.
        if box_count[min_index] == 0:
            min_index += 1

        box_count[min_index] -= 1        # 작은 박스 높이 커졌으니까 개수 하나 줄이고
        box_count[min_index + 1] += 1    # 그 다음 작은 박스 높이는 커짐

        count += 1

    print(f'#{test_case + 1} {max_index - min_index}')

# # count sort로 풀기
# for test_case in range(10):
#     dump_count = int(input())
#     box_list = list(map(int, input().split()))

#     box_count = [0] * 101  # 박스 최대 높이 100
#     box_count[0] = 100 - len(box_list)
#     for i in range(len(box_list)):
#         box_count[box_list[i]] += 1

#     count = 0
#     max_index = 100 # 최대 박스 높이
#     min_index = 0   # 최저 박스 높이
#     while box_count[max_index] == 0:
#         max_index -= 1
#     while box_count[min_index] == 0:
#         min_index += 1

#     while count < dump_count:
#         count += 1
#         # 최대 박스 높이에 박스 있으면 박스하나 빼서
#         box_count[max_index] -= 1
#         box_count[max_index - 1] += 1
#         box_count[min_index] -= 1        # 작은 박스 높이 커졌으니까 개수 하나 줄이고
#         box_count[min_index + 1] += 1    # 그 다음 작은 박스 높이는 커짐

#         # 최대 박스 높이에 박스 없으면 작은쪽에 있나 보기
#         if box_count[max_index] == 0:
#             max_index -= 1
#         # 제일 낮은 높이에 박스 넣어준다.
#         if box_count[min_index] == 0:
#             min_index += 1


#     print(f'#{test_case + 1} {max_index - min_index}')

