import math

def get_fee(fees, used_time):
    base_time, base_fee, unit, unit_fee = fees
    fee = base_fee
    if used_time <= base_time:
        return fee
    over_time = used_time - base_time
    fee += math.ceil(over_time / unit) * unit_fee
    return fee

def get_used_time(in_time, out_time):
    in_time = 60*int(in_time[0:2]) + int(in_time[3:5])
    out_time = 60*int(out_time[0:2]) + int(out_time[3:5])
    used_time = out_time - in_time
    return used_time


def solution(fees, records):
    answer = []
    used_times = dict()
    in_times = dict()
    for record in records:
        time, car, action = record.split()
        if action == "IN":
            in_times[car] = time
        if action == "OUT":
            if car not in used_times.keys():
                used_times[car] = 0
            used_times[car] += get_used_time(in_times[car], time)
            del in_times[car]
    for car in in_times:
        if car not in used_times.keys():
            used_times[car] = 0
        used_times[car] += get_used_time(in_times[car], "23:59")
    car_list = sorted(used_times.keys())
    for car in car_list:
        answer.append(get_fee(fees, used_times[car]))


    return answer
