# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

# 1. int형으로만 접근
a, b = map(int, input().split())

# 100의 자리수 -> 1의 자리수, 10의 자리수, 1의 자리수 -> 100의 자리수
# 734 = 700 + 30 + 4
# 7 = 734 // 100
# 3 = (734 - ((734 // 100) * 100)) // 10 = 34 // 10
# 4 = 734 % 10

new_a = a // 100 + (a - a // 100 * 100) // 10 * 10 + a % 10 * 100
new_b = b // 100 + (b - b // 100 * 100) // 10 * 10 + b % 10 * 100

print(max(new_a, new_b))

# 2. str로 접근
a, b = map(str, input().split())
new_a = int(a[::-1])
new_b = int(b[::-1])
print(max(new_a, new_b))