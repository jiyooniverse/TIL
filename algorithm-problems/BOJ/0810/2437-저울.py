# 저울

N = int(input())
weight_list = list(map(int, input().split()))

# 무게 리스트 정렬
for i in range(N-1,1,-1):
    for j in range(0, i):
        if weight_list[j] > weight_list[j + 1]:
            weight_list[j], weight_list[j + 1] = weight_list[j + 1], weight_list[j]

find_weight = 1
for weight in weight_list:
    if find_weight + 1 > weight:
        find_weight += weight
    else:
        break






# # min_weight = 1

# # while True:
# #     if min_weight in weight_list:
# #         weight = min_weight # 있는 것 중에 가장 큰 것
# #         min_weight += 1
# #         continue
    
# #     # 찾을 무게
# #     find_weight = min_weight - weight

# #     # 찾을 무게가 리스트에 있으면 

# weight_count = [0]*10000
# for weight in weight_list:
#     weight_count[weight] += 1

# find_weight = 1     # 찾을 무게
# while True:
#     if weight_count[find_weight] != 1:
#         find_weight += 1
#         continue

#     tmp = find_weight
#     tmp_count = weight_count[:]
#     for i in range(tmp-1, 0, -1):
#         if tmp_count[i] != 0:
#             tmp -= i
#             tmp_count[i] -= 1
    

    