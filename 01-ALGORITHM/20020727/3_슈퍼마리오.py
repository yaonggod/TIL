# https://www.acmicpc.net/problem/2851
mushroom = []
for i in range(10):
    mushroom.append(int(input()))
# 0, 0 + 1, 0 + 1 + 2, ....
# 나올 수 있는 score의 모든 경우
score = []
for i in range(1, 11):
    sum_mushroom = 0
    for j in range(i):
        sum_mushroom += mushroom[j]
    score.append(sum_mushroom)
# score을 100을 기준으로 나눔
score_under_100 = []
score_over_100 = []
for i in range(10):
    if score[i] <= 100:
        score_under_100.append(score[i])
    else:
        score_over_100.append(score[i])

# 점수들이 100을 기준으로 한쪽으로만 쏠려있는 경우
if score_under_100 == []:
    print(min(score_over_100))
elif score_over_100 == []:
    print(max(score_under_100))

# 100보다 큰 값중 제일 작은 값과 100보다 작은 값 중 제일 큰 값을 비교       
elif abs(100 - max(score_under_100)) > abs(100 - min(score_over_100)):
    print(min(score_over_100))
elif abs(100 - max(score_under_100)) == abs(100 - min(score_over_100)):
    print(min(score_over_100))   
else:
    print(max(score_under_100))