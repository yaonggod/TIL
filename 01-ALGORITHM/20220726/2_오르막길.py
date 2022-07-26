# https://www.acmicpc.net/problem/2846
n = int(input())
lst = list(map(int, input().split()))

height = 0
height_lst = []
for i in range(n - 1):
    # 오르막길이 지속될 시 height 갱신
    # height_lst에 지속적으로 업데이트해야 앞의 height 정보를 기록할 수 있음
    if lst[i] < lst[i + 1]:
        height += lst[i + 1] - lst[i]
        height_lst.append(height)
    # 오르막길이 멈출 시 height 0으로 초기화
    else:
        height = 0
if height_lst:
    print(max(height_lst))
else:
    print(0)