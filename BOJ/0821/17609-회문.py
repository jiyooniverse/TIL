# BOJ 17609 회문
n = int(input())

for i in range(n):
    pal = input()
    # 회문: 0, 유사회문: 1, 그 외: 2
    res = 2
    if pal == pal[::-1]:
        res = 0
    else:
        # 유사 회문인지 확인
        for j in range(len(pal)//2 + 1):
            if pal[j] == pal[-1 - j]:
                continue
            else:
                # 1) 앞에 하나 밀어서 비교
                temp = pal[j+1:len(pal)-j]
                if temp == temp[::-1]:
                    res = 1
                # 2) 뒤에 하나 땡겨서 비교
                temp = pal[j: -j-1]
                if temp == temp[::-1]:
                    res = 1
                # 3) 위에 다 확인 했으면 나가자
                break
    print(res)
