# 수 이어가기

# 첫 번째 수
num = int(input())

def num_check(num2):
    num1 = num
    num_list = [num1, num2]
    num3 = num1 - num2
    while num3 >= 0:
        num_list.append(num3)
        num1, num2 = num2, num3
        num3 = num1 - num2

    return num_list

result = []
max_count = 0
for i in range(num+1):
    count = len(num_check(i))
    if max_count < count:
        max_count = count
        result = num_check(i)[:]

print(max_count)
for i in range(max_count):
    print(result[i], end=' ')