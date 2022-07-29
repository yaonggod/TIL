import sys

sys.stdin = open("_직사각형길이찾기.txt")

t = int(input())
for i in range(1, t + 1):
    a, b, c = map(int, input().split())
    # 정사각형인 경우 아무 값이나 출력
    if a == b == c:
        print("#{}".format(i), a)
    # 정사각형이 아닌 직사각형의 경우 한 번만 나온 값을 출력
    elif a == b:
        print("#{}".format(i), c)
    elif b == c:
        print("#{}".format(i), a)
    else:
        print("#{}".format(i), b)