from itertools import combinations

def solution(relation):
    keys = dict()
    attributes = list(range(len(relation[0])))
    for i in range(1, len(attributes)+1):
        keys[i] = []
        groups = combinations(attributes, i)
        for group in groups:
            data_list = []
            temp = [0]*len(group)
            is_key = True
            for student in range(len(relation)):
                for attribute in range(len(group)):
                    temp[attribute] = relation[student][group[attribute]]
                if temp in data_list:
                    is_key = False
                    break
                else:
                    data_list.append(temp[:])
            if is_key:
                keys[i].append(set(group))
    candidate_keys = []
    for i in range(1, len(attributes)+1):
        for key in keys[i]:
            candidate_keys.append(key)

    for i in range(1, len(attributes)):
        for key in keys[i]:
            for j in range(i+1, len(attributes)+1):
                for biggerkey in keys[j]:
                    if key <= biggerkey and biggerkey in candidate_keys:
                        candidate_keys.remove(biggerkey)

    return len(candidate_keys)
