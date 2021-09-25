# BOJ 17413 단어 뒤집기 2
S = input()

result = ""
new_s = ""
flag = 0
for i in range(len(S)):
    if S[i] == "<":
        flag = 1

    if flag == 1:   # "<"와 ">" 사이
        new_s += S[i]
    elif S[i] == " ":   # 공백일떄
        result += new_s + " "
        new_s = ""
    else:
        new_s = S[i] + new_s

    if S[i] == ">":
        result += new_s
        new_s = ""
        flag = 0

result += new_s

print(result)
