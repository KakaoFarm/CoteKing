import bisect

def solution(info, query):
    answer = []
    applicants = [[[[[] for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(4)]
    for applicant in info:
        lang, group, career, food, score = applicant.split()
        if lang == "cpp":
            lang = 1
        elif lang == "java":
            lang = 2
        else: lang = 3
        if group == "backend":
            group = 1
        else: group = 2
        if career == "junior":
            career = 1
        else: career = 2
        if food == "chicken":
            food = 1
        else: food = 2
        score = int(score)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    for l in range(2):
                        applicants[i*lang][j*group][k*career][l*food].append(score)
    for i in range(4):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        applicants[i][j][k][l].sort()

    for filter in query:
        count = 0
        filter_list = filter.split()
        if filter_list[0] == "cpp":
            lang = 1
        elif filter_list[0] == "java":
            lang = 2
        elif filter_list[0] == "python":
            lang = 3
        else: lang = 0
        if filter_list[2] == "backend":
            group = 1
        elif filter_list[2] == "frontend":
            group = 2
        else: group = 0
        if filter_list[4] == "junior":
            career = 1
        elif filter_list[4] == "senior":
            career = 2
        else: career = 0
        if filter_list[6] == "chicken":
            food = 1
        elif filter_list[6] == "pizza":
            food = 2
        else: food = 0
        score = int(filter_list[7])
        count = len(applicants[lang][group][career][food]) - bisect.bisect_left(applicants[lang][group][career][food],score)
        answer.append(count)

    return answer
