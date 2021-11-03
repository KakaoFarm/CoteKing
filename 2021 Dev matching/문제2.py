def is_holy(first_day, cur_day):
    if (cur_day + first_day - 1) % 7 in [6, 0]:
        return True
    else:
        return False
 
def solution(leave, day, holidays):
    if day == "MON":
        day = 1
    elif day == "TUE":
        day = 2   
    elif day == "WED":
        day = 3   
    elif day == "THU":
        day = 4   
    elif day == "FRI":
        day = 5   
    elif day == "SAT":
        day = 6   
    elif day == "SUN":
        day = 0   
    
    answer = -1
    for start in range(1, 31):
        cur = start
        remaining_leave = leave
        count = 0
        while cur <= 30:
            if is_holy(day, cur) or cur in holidays:
                count += 1
            elif remaining_leave > 0:
                remaining_leave -= 1
                count += 1
            else:
                break
            cur += 1
        answer = max(answer, count)
                
    return answer