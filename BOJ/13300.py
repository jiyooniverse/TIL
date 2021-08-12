# BOJ - 13300 방배정

n, k = map(int, input().split())    # 학생수, 한 방 최대 인원
students = [[0] * 7 for _ in range(2)]
for i in range(n):
    # 성별, 학년
    gender, grade = map(int, input().split())
    students[gender][grade] += 1

room = 0
for i in range(1, len(students[0])):
    room += (students[0][i] + k - 1) // k    # 여학생
    room += (students[1][i] + k - 1) // k  # 남학생

print(room)
