# https://www.acmicpc.net/problem/2953
scores = []
# 리스트 안에 리스트 넣기
for i in range(5):
    scores.append(list(map(int, input().split())))

# 점수의 총합으로 구성된 새로운 리스트 생성
total_score = []
for score in scores:
    total_score.append(sum(score))
    
max_score = max(total_score)
# 1번 참가자부터 있으므로 index에 1 더해주기
print(total_score.index(max_score) + 1, max_score)