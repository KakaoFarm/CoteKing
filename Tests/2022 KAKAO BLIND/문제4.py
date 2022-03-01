def better_answer(answer1, answer2, i):
    if answer1 == answer2:
        return answer1
    for k in range(i+1):
        if answer1[k] > answer2[k]:
            return answer1
        if answer1[k] < answer2[k]:
            return answer2

def solution(n, info):
    gap = 0
    for i in range(11):
        if info[i] != 0:
            gap -= (10-i)
    arrows_to_score = dict()
    for i in range(1, 11):
        if info[10-i] == 0:
            arrows_to_score[i] = (1, i)
        if info[10-i] != 0:
            arrows_to_score[i] = (info[10-i] + 1, 2*(i))
    dp = [[[gap,[0]*11] for _ in range(n+1)] for _ in range(11)]
    topscore = gap
    for i in range(1, 11):
        required_arrows, score = arrows_to_score[i]
        for arrows in range(1, n+1):
            if required_arrows <= arrows:
                dp[i][arrows][0] = max(dp[i-1][arrows][0], dp[i-1][arrows-required_arrows][0] + score)
                if dp[i-1][arrows-required_arrows][0] + score > dp[i-1][arrows][0]:
                    dp[i][arrows][1] = dp[i-1][arrows-required_arrows][1][:]
                    dp[i][arrows][1][i] = required_arrows
                    if dp[i][arrows][0] > topscore:            
                        topscore= dp[i][arrows][0]
                        answer = dp[i][arrows][1]
                    elif dp[i][arrows][0] == topscore:
                        answer = better_answer(answer, dp[i][arrows][1], i)
                elif dp[i-1][arrows-required_arrows][0] + score == dp[i-1][arrows][0]:
                    dp[i][arrows][1] = dp[i-1][arrows-required_arrows][1][:]
                    dp[i][arrows][1][i] = required_arrows
                    dp[i][arrows][1] = better_answer(dp[i][arrows][1], dp[i-1][arrows][1], i)
                    if dp[i][arrows][0] > topscore:            
                        topscore= dp[i][arrows][0]
                        answer = dp[i][arrows][1]
                    elif dp[i][arrows][0] == topscore:
                        answer = better_answer(answer, dp[i][arrows][1], i)
                else:
                    dp[i][arrows][1] = dp[i-1][arrows][1][:]
            else:
                dp[i][arrows][0] = dp[i-1][arrows][0]
                dp[i][arrows][1] = dp[i-1][arrows][1][:]
    if dp[10][n][0] <= 0:
        return [-1]
    answer = answer[::-1]
    if sum(answer) < n:
        answer[10] += n - sum(answer)
    return answer

## 시험 끝나고 고친 거라 맞는지 모르겠음..
