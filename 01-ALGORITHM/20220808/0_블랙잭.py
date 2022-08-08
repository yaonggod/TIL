n, m = map(int, input().split())
lst = list(map(int, input().split()))

# 나올 수 있는 모든 합의 경우
sum_card = []
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            sum_card.append(lst[i] + lst[j] + lst[k])
sum_card = sorted(sum_card)
# 조건에 맞는 max값을 찾아나감
max = sum_card[0]
for i in range(len(sum_card)):
    if sum_card[i] > max and sum_card[i] <= m:
        max = sum_card[i]
print(max)