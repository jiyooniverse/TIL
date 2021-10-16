# 구간합

T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())   # 구간 개수
    num_list = list(map(int, input().split()))

    max_sum = num_list[0]
    min_sum = sum(num_list)

    # i번부터 M개씩 더한다.
    for i in range((N+1) -M):
        total = 0
        for j in range(M):
            total += num_list[i + j]
        if total > max_sum:
            max_sum = total
        if total < min_sum:
            min_sum = total
    result = max_sum - min_sum

    print(f'#{test_case + 1} {result}')


"""
 다른 풀이 
 prefix : 합을 미리 구해놓는 방법
 prefix[index] <- 0 ~ index번까지의 합
 [S~E] <- [0 ~ E] - [0 ~ S] + [S]
 
 원본 : arr[]
 합 : prefix[]
 sum = prefix[E] - prefix[S] + arr[S]
"""
#  # 2. prefix
# T = int(input())
# for tc in range(T):
#     n, m = map(int, input().split())
#     num_li = list(map(int, input().split()))
#     prefix = [0] * n
#     prefix[0] = num_li[0] # 0번 = 원본 0번과 같은 값
#     for i in range(1, n):
#         prefix[i] = prefix[i - 1] + num_li[i]
#     # prefix[i] : 0~i번까지의 num_li들의 합
#
#     """
#     5 ~ 9
#     #[5~9]= [0~9]     - [0 ~ 5]   + [5]
#     sum = prefix[9] - prefix[5] + num_li[5]
#     """
#     max_value = -1
#     min_value = 100 * 10000 + 1
#     for s in range(n - m + 1): # 구간의 시작점 s
#         e = s + m - 1 # 구간의 끝점 e
#         # s ~ e(s ~ s+m-1) m개 data들의 합
#         sum = prefix[e] - prefix[s] + num_li[s]
#         if max_value < sum :
#             max_value = sum
#         if min_value > sum :
#             min_value = sum
#
#     # 모든 m 구간크기내에 합
#     # 최댓값, 최솟값
#
#     print("#{} {}".format(tc+ 1, max_value - min_value))

# 3. sliding window
# T = int(input())
# for tc in range(T):
#     n, m = map(int, input().split())
#     num_li = list(map(int, input().split()))
#
#     sum = 0
#     for i in range(m - 1):
#         sum += num_li[i]
#         # m-1개의 합
#
#     max_value = -1
#     min_value = 100 * 10000 + 1
#
#     for s in range(n - m + 1):
#         e = s + m - 1
#         # s ~ e(s~s+m-1) 총 m개 DATA
#
#         sum += num_li[e] # 새로 추가되어야 하는 DATA 추가(m개짜리 합)
#
#         if max_value < sum :
#             max_value = sum
#         if min_value > sum :
#             min_value = sum
#         # 처리
#
#         sum -= num_li[s]
#         # 다음 구간에 필요없는 data 삭제(m-1개 합)
#
#     print("#{} {}".format(tc+ 1, max_value - min_value))