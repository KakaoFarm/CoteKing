def time_to_int(time):
    hour = int(time[0:2])
    minute = int(time[3:5])
    second = int(time[6:8])
    int_time = hour*3600 + minute*60 + second
    return int_time

def solution(play_time, adv_time, logs):
    adv_time = time_to_int(adv_time)
    play_time = time_to_int(play_time)
    start_times = [0]*(play_time+1)
    end_times = [0]*(play_time+1)
    for i in range(len(logs)):
        start = time_to_int(logs[i][0:8])
        end = time_to_int(logs[i][9:17])
        start_times[start] += 1
        end_times[end] += 1
    answer = 0
    maximum_view = 0
    view = 0
    counter = sum(start_times[:adv_time]) - sum(end_times[:adv_time])
    for start_time in range(1, play_time - adv_time + 1):
        end_time = start_time + adv_time
        counter = counter + start_times[end_time-1] - end_times[end_time-1] - start_times[start_time-1] + end_times[start_time-1]
        view += counter
        if view > maximum_view:
            maximum_view = view
            answer = start_time
        print(start_time, end_time, view)
    hour = answer // 3600
    minute = (answer % 3600) // 60
    second = answer % 60
    answer = f"{hour:0>2}:{minute:0>2}:{second:0>2}"
    return answer
