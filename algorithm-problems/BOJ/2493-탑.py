# BOJ 2493 탑
n = int(input())
height = list(map(int, input().split()))
stack = []
index = []
result = [0] * n
for i in range(n):
    while len(stack) > 0:
        if stack[-1] < height[i]:
            stack.pop()
            index.pop()
        else:
            break
    if len(stack) == 0:
        result[i] = 0
    else:
        result[i] = index[-1]
    stack.append(height[i])
    index.append(i + 1)

print(" ".join(str(s) for s in result))


