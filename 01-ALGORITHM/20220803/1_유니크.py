# https://www.acmicpc.net/problem/5533
n = int(input())
game = []
for i in range(n):
    game.append(list(map(int, input().split())))

# 게임별로 각 사람의 n - 1번째 인덱스의 제출 결과 저장
game1 = []
game2 = []
game3 = []
for i in range(n):
    game1.append(game[i][0])
    game2.append(game[i][1])
    game3.append(game[i][2])

# 제출 결과의 count가 1일시에만 점수로 인정
for i in range(n):
    score = 0
    if game1.count(game[i][0]) == 1:
        score += game[i][0]
    if game2.count(game[i][1]) == 1:
        score += game[i][1]
    if game3.count(game[i][2]) == 1:
        score += game[i][2]
    print(score)