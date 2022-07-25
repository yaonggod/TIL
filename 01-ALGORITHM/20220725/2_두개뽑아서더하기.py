# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    # (0, 1), (0, 2), ... (0, n)
    # (1, 2), (1, 3), ... (1, n)
    # (n - 2, n - 1), (n - 2, n)
    # (n - 1, n)
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    # 정렬 후 set으로 만들어 중복 제거
    answer.sort()
    # set을 다시 list로 만들어 정렬
    answer = sorted(list(set(answer)))
    return answer



print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
