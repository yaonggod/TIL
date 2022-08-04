# https://www.acmicpc.net/problem/1652
n = int(input())
matrix = [list(input()) for _ in range(n)]
# 행과 열이 뒤집힌 matrix
new_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_matrix[i][j] = matrix[j][i]

# 가로줄 검증
row = 0
for i in range(n):
    stack_row = []
    for j in range(n):
        if matrix[i][j] == '.':
            stack_row.append('.')
        elif matrix[i][j] == 'X':
            if len(stack_row) >= 2:
                row += 1
                stack_row.clear()
            else:
                stack_row.clear()
    if len(stack_row) >= 2:
        row += 1
    
        
# 세로줄 검증
column = 0
for i in range(n):
    stack_column = []
    for j in range(n):
        if new_matrix[i][j] == '.':
            stack_column.append('.')
        elif new_matrix[i][j] == 'X':
            if len(stack_column) >= 2:
                column += 1
                stack_column.clear()
            else:
                stack_column.clear()
    if len(stack_column) >= 2:
        column += 1
        
print(row, column)