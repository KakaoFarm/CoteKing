
def solution(food_times, k):
    food_ranking = sorted(food_times)
    remaining_food = len(food_times)
    prev_eaten = 0
    eaten = 0
    count = 0
    for food in food_ranking:
        if prev_eaten != food:
            k -= eaten * remaining_food
            eaten = food - prev_eaten
            if k < 0:
                break
            prev_eaten = food
            remaining_food -= count
            count = 0
        count += 1
    if k >= 0: 
        k -= eaten * remaining_food
    if k >= 0:
        return -1
    
    count_remaining =  0
    target = k % remaining_food
    for i in range(len(food_times)):
        if food_times[i] >= prev_eaten:
            if count_remaining == target:
                return i+1
            else:
                count_remaining += 1
