# https://www.acmicpc.net/problem/3052

# 리스트 사용
lst = []

for i in range(1, 11):
    lst.append(int(input()))
    
new_list = []

for i in range(0, len(list)):
    if lst[i] % 42 in new_list:
        continue
    else:
        new_list.append(lst[i] % 42)
    
print(len(new_list))


# 딕셔너리 사용
number_dict = {}
for i in range(10):
    n = int(input())
    if n % 42 not in number_dict:
        number_dict[n % 42] = 1
    else:
        number_dict[n % 42] += 1
print(len(number_dict))