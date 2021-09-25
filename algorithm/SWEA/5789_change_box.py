# 현주의 상자 바꾸기

T = int(input())

for test_case in range(T):
    N, Q = map(int, input().split())
    box_list = [0] * N
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L - 1, R):
            box_list[j] = i
    result = ' '.join(str(box) for box in box_list)
    print(f'#{test_case + 1} {result}')



# T = int(input())
# for tc in range(T):
#     N, Q = map(int, input().split())
#
#     li = [0] * (N + 1)
#     # li[index] => index : 0 ~ N <- 1~N
#     for i in range(1, Q + 1):
#         L, R = map(int, input().split())
#         # list[L ~ R] = i
#         # L~R : 1~N
#         for j in range(L, R + 1):
#             # j -> L ~ R
#             li[j] = i
#     print("#{} ".format(tc + 1), end = "")
#     for i in range(1, N+1):
#         print("{} ".format(li[i]), end = "")
#     print("")
