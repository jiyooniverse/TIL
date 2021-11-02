# 12813 이진수 연산
A = list(map(int, input()))
B = list(map(int, input()))


for k in range(5):
    res = ''
    if k == 0:
        for i in range(len(A)):
            res += str(A[i] & B[i])
        print(res)
    elif k == 1:
        for i in range(len(A)):
            res += str(A[i] | B[i])
        print(res)
    elif k == 2:
        for i in range(len(A)):
            res += str(A[i] ^ B[i])
        print(res)
    elif k == 3:
        for i in range(len(A)):
            res += str(A[i] ^ 1)
        print(res)
    elif k == 4:
        for i in range(len(A)):
            res += str(B[i] ^ 1)
        print(res)

