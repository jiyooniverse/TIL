# BOJ 10158 개미

w, h = map(int, input().split())    # 가로, 세로길이
p, q = map(int, input().split())    # 초기 위치
time = int(input())                 # 주어진 시간


m_p = (p + time) // w
r_p = (p + time) % w
m_q = (q + time) // h
r_q = (q + time) % h

if m_p % 2 == 0: # 정방향으로 가면
    p = r_p
else:
    p = w - r_p

if m_q % 2 == 0: # 정방향으로 가면
    q = r_q
else:
    q = h - r_q

print(p, q)


# 시간 초과 :  time <= 200,000,000
# dir_p = dir_q = 1   # 초기 방향 둘다 양의 방향으로
# for t in range(time):   # 1시간이 지날때마다 대각 방향으로 1, 1씩 움직인다.
#     next_p = p + dir_p
#     next_q = q + dir_q
#     if 0 <= next_p <= w:
#         p = next_p
#     else:
#         dir_p *= -1
#         p = p + dir_p
#
#     if 0 <= next_q <= h:
#         q = next_q
#     else:
#         dir_q *= -1
#         q = q + dir_q
#
# print(p, q)
