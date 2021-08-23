def get_up_down_needed(alphabet):
    return min(ord(alphabet)-65, 91-ord(alphabet))

def get_zero_in_a_row(start,direction,list,count):
    try:
        if list[start] == 0 and count + 1 < len(list):
            count += 1
            return get_zero_in_a_row(start+direction,direction,list,count)
        else:
            return count
    except:
        return count


def solution(name):
    name = list(map(get_up_down_needed, list(name)))
    answer = sum(name) + len(name) - 1
    zero_in_a_row_left = get_zero_in_a_row(-1,-1,name,0)
    zero_in_a_row_right = get_zero_in_a_row(1,1,name,0)
    zero_in_a_row_max = max(zero_in_a_row_left, zero_in_a_row_right)
    answer -= zero_in_a_row_max
    return answer

print(solution("AAAA"))

# Greedt 하지 않다는 문제 오류가 있다고 해서 여기까지만 하고 포기..