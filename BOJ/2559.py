# 수열

######### 시간 초과 #########
# N : 온도 측정 전체 날짜 (2이상 100,000이하)
# K : 연속되는 날짜
#
# n, k = map(int, input().split())
# days = list(map(int, input().split()))
#
# max_sum = 0
# for i in range(k):
#     max_sum += days[i]
#
# tmp_sum = 0
# for s in range((n+1)-k):    # 시작 날짜
#     for i in range(k):
#         tmp_sum += days[s + i]
#     if tmp_sum > max_sum:
#         max_sum = tmp_sum
#
# print(max(max_sum))

n, k = map(int, input().split())
days = list(map(int, input().split()))

max_sum = 0
for i in range(k):
    max_sum += days[i]
tmp_sum = 0
for i in range(k - 1):
    tmp_sum += days[i]
for s in range((n + 1) - k):  # 시작 날짜
    e = s + k - 1
    tmp_sum += days[e]
    if tmp_sum > max_sum:
        max_sum = tmp_sum
    tmp_sum -= days[s]

print(max_sum)
