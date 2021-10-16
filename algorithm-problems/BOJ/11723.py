# 11723 집합
import sys

M = int(sys.stdin.readline().rstrip())

# check = [0] * 21
# for i in range(M):
#     cmd = sys.stdin.readline().split()
#     if cmd[0] == 'add':
#         x = int(cmd[1])
#         if check[x] == 0:
#             check[x] = 1
#     elif cmd[0] == 'remove':
#         x = int(cmd[1])
#         if check[x] == 1:
#             check[x] = 0
#     elif cmd[0] == 'toggle':
#         x = int(cmd[1])
#         check[x] = check[x] ^ 1
#
#     elif cmd[0] == 'check':
#         x = int(cmd[1])
#         print(check[x])
#
#     elif cmd[0] == 'all':
#         check = [1] * 21
#
#     elif cmd[0] == 'empty':
#         check = [0] * 21


## 비트 마스크 이용
check = 0
for _ in range(M):
    command = sys.stdin.readline().split()
    if command[0] == 'empty':
        check = 0
    elif command[0] == 'all':
        check = (1 << 21) - 1
    else:
        n = int(command[1])
        if command[0] == 'add':
            check = check | (1 << n)
        elif command[0] == 'toggle':
            check = check ^ (1 << n)
        elif command[0] == 'remove':
            tmp = ((1 << 21) - 1) ^ (1 << n)
            check = check & tmp
        elif command[0] == 'check':
            print(1) if check & (1 << n) != 0 else print(0)

