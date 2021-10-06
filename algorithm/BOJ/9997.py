# 9997 폰트
import sys
N = int(sys.stdin.readline())
book = [0] * N
for i in range(N):
    word = sys.stdin.readline().rstrip()
    # 각 단어의 위치가 1이 되도록
    for w in word:
        book[i] |= 1 << (ord(w) - ord('a'))   # 'a'가 0번째가 되도록 밀고 or 연산해서 w마다 해주기


# 테스트 문장에는 알파벳 소문자 26개가 모두 들어있어야한다. (1 << 26 - 1)

# book에서 단어 몇개 꺼내서 알파벳 26자 다 들어있는지 확인
def dfs(now, res=0):
    # print(res)
    global cnt
    if res == (1 << 26) - 1:
        cnt += 1


    # dfs(now + 1, res+book[now + 1])
    # dfs(now + 1, res)
    for i in range(now, N):
        if check[i] == 0:
            check[i] = 1
            dfs(i, res|book[i])     # or연산자로 합쳐주기
            check[i] = 0


check = [0] * N     # 사용한 단어인지 확인한다.
cnt = 0
dfs(0)
print(cnt)
