# https://www.acmicpc.net/problem/1543
document = input()
word = input()
index_list = [i for i in range(len(document))]
count = 0
for i in range(len(document) - len(word) + 1):
    # 검사하는 위치의 첫 번째 인덱스만 존재하는 것을 확인하면 검사 가능
    if document[i:i + len(word)] == word and i in index_list:
        count += 1
        # 검사 후 일치한 인덱스는 지움
        for j in range(i, i + len(word)):
            index_list.remove(j)
print(count)
        
    