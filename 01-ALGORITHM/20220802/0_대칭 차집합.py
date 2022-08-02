# https://www.acmicpc.net/problem/1269
a, b = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

set_a_minus_b = set_a - set_b
set_b_minus_a = set_b - set_a

print(len(set_a_minus_b) + len(set_b_minus_a))