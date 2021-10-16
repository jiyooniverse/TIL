# 14888 연산자 끼워넣기
# 식의 결과가 최대인 것과 최소인 것
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))    # 덧셈, 뺄셈, 곱셈, 나눗셈


def dfs(now, total):
    global min_ans, max_ans
    if now == N - 1:
        if total > max_ans:
            max_ans = total
        if total < min_ans:
            min_ans = total
        return

    for k in range(4):
        if op[k] < 1: continue

        if k == 0:
            new_total = total + num[now + 1]
        elif k == 1:
            new_total = total - num[now + 1]
        elif k == 2:
            new_total = total * num[now + 1]
        elif k == 3:
            minus = 1
            if total < 0:
                minus = -1
            new_total = ((minus*total) // num[now + 1]) * minus

        op[k] -= 1
        dfs(now + 1, new_total)
        op[k] += 1


min_ans = 987654321
max_ans = -987654321
# 맨처음 값 넣고 시작
dfs(0, num[0])
print(max_ans)
print(min_ans)
