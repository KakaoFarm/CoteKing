def solution(n, text, second):
    full = "_"*n + text.replace(" ", "_")
    m = len(full)
    
    i = (second) % m
    j = (i + n - 1) % m
    if i < j:
        answer = full[i:j+1]
    else: 
        answer = full[i:] + full[:j+1]
    return answer