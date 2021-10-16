# BOJ 9935 문자열 폭발

str1 = input()
str2 = input()
stack = []
for now in str1:
    stack.append(now)
    if now == str2[-1] and len(stack) >= len(str2):
        str_list = list(str2)
        if stack[-len(str2)::] == str_list:
            for i in range(len(str2)):
                stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(str(s) for s in stack))
