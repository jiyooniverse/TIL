# 2504 괄호의 값

bracket = list(input().rstrip())

i = 0
find = []
num = []
res = 0
while i < len(bracket):
    if bracket[i] == '(':
        find.append(')')
        num.append(0)
    elif bracket[i] == '[':
        find.append(']')
        num.append(0)
    elif len(find) > 0 and bracket[i] == find[-1]:
        if bracket[i] == ')':
            if bracket[i - 1] == ')' or bracket[i - 1] == ']':
                num_len = len(num)
                for k in range(num_len - 1, -1, -1):
                    if num[k] == 0:
                        num.pop(k)
                        break
                    num[k] *= 2

            else:
                num.pop(-1)
                num.append(2)
        else:
            if bracket[i - 1] == ')' or bracket[i - 1] == ']':
                num_len = len(num)
                for k in range(num_len - 1, -1, -1):
                    if num[k] == 0:
                        num.pop(k)
                        break
                    num[k] *= 3
            else:
                num.pop(-1)
                num.append(3)

        find.pop(-1)
    else:
        res = 0
        num.clear()
        break

    i += 1

if len(find) == 0:
    for j in range(len(num)):
        res += num[j]

print(res)

