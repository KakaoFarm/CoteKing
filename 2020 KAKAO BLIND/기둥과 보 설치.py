def is_valid(type, location, pillars, bos):
    x, y = location
    if type == "pillar":
        if y == 0:
            return True
        elif y > 0 and pillars[x][y-1]:
            return True
        elif (x > 0 and bos[x-1][y]) or bos[x][y]:
            return True
        else:
            return False
    if type == "bo":
        if pillars[x][y-1] or pillars[x+1][y-1]:
            return True
        elif (x > 0 and bos[x-1][y] and bos[x+1][y]):
            return True
        else:
            return False

def solution(n, build_frame):
    answer = []
    pillars = [[0]*(n+1) for _ in range(n+1)]
    bos = [[0]*(n+1) for _ in range(n+1)]
    for action in build_frame:
        x = action[0]
        y = action[1]
        if action[2] == 0: #기둥
            if action[3] == 0: #기둥 삭제
                pillars[x][y] = 0
                if (pillars[x][y+1] and not is_valid("pillar", (x, y+1), pillars, bos)) or (y < n and bos[x][y+1] and not is_valid("bo", (x, y+1), pillars, bos)) or (x > 0 and bos[x-1][y+1] and not is_valid("bo", (x-1, y+1), pillars, bos)):
                    pillars[x][y] = 1
            if action[3] == 1: #기둥 건설
                if is_valid("pillar", (x, y), pillars, bos):
                    pillars[x][y] = 1
        elif action[2] == 1: #보
            if action[3] == 0: #보 삭제
                bos[x][y] = 0
                if (pillars[x][y] and not is_valid("pillar", (x, y), pillars, bos)) or (pillars[x+1][y] and not is_valid("pillar", (x+1, y), pillars, bos)) or (x > 0 and bos[x-1][y] and not is_valid("bo", (x-1, y), pillars, bos)) or (bos[x+1][y] and not is_valid("bo", (x+1, y), pillars, bos)):
                    bos[x][y] = 1
            if action[3] == 1: #보 건설
                if is_valid("bo", (x, y), pillars, bos):
                    bos[x][y] = 1
    for i in range(n+1):
        for j in range(n+1):
            if pillars[i][j] == 1:
                answer.append([i, j, 0])
            if bos[i][j] == 1:
                answer.append([i, j, 1])
    return answer

solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
