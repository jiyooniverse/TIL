# BOJ 2605 줄세우기 
n = int(input())
students = list(map(int, input().split()))
line = []
for i in range(n):
    k = i - students[i]
    line.insert(k, i + 1)

line_str = " ".join(str(n) for n in line)
print(line_str)