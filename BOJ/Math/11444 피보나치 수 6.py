def multiple(x, y):
    answer = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            answer[i][j] = (x[i][0]*y[0][j] + x[i][1]*y[1][j])%1000000007
    return answer


B = str(format(int(input()), 'b'))

matrices = [[[1, 1], [1, 0]]]
for _ in range(len(B)-1):
    matrices.append(multiple(matrices[-1], matrices[-1]))

answer = [[1, 0], [0, 1]]
for i in range(len(B)):
    if B[i] == "1":
        answer = multiple(matrices[-i-1], answer)
print(answer[1][0])
