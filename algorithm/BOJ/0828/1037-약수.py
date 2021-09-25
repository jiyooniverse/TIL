# BOJ 1037 약수
N = int(input())
arr = list(map(int, input().split()))
# 오름차순 정렬 후
arr.sort()

result = arr[0] * arr[-1]
print(result)
