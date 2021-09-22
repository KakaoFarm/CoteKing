notes = list(map(int, input().split())) 
answer = float('INF')
if len(notes) == 2:
    answer = 2
elif len(notes) == 1:
    answer = 0
first_note = notes[0]
notes = notes[1:-1]

def solution(notes, scores):
    for note in notes:
        new_scores = dict()
        for state in scores.keys():
            if note in state:
                if state not in new_scores.keys():
                    new_scores[state] = scores[state] + 1
                else:
                    new_scores[state] = min(new_scores[state], scores[state]+1)
            else:
                for foot in state:
                    if foot == 0:
                    	energy = 2
                    elif abs(foot - note) == 2:
                        energy = 4
                    else:
                        energy = 3
                    new_state = frozenset((state | {note}) - {foot})
                    if new_state not in new_scores.keys():
                        new_scores[new_state] = scores[state] + energy
                    else:
                        new_scores[new_state] = min(new_scores[new_state], scores[state]+energy)
        scores = new_scores
    return new_scores

initial_state = frozenset([0, first_note])
initial_score = {initial_state: 2}
if len(notes) > 0:
    scores = solution(notes, initial_score)
    for score in scores:
        answer = min(scores[score], answer)
print(answer)
