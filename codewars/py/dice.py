from collections import Counter

def score(dice):
    # your code here
    scores = Counter(dice)
    uniques = set(dice)
    total = 0
    scores_dict = {
        '3_1': 1000,
        '3_2': 200,
        '3_3': 300,
        '3_4': 400,
        '3_5': 500,
        '3_6': 600,
        '1_5': 50,
        '1_1': 100
    }
    for u in uniques:
        if scores[u] == 3:
            u_score_key = f'3_{u}'
            total += scores_dict[u_score_key]
            continue
        elif scores[u] > 3:
            u_score_key = f'3_{u}'
            total += scores_dict[u_score_key]
            if u in (1, 5):
                diff = scores[u] - 3
                total += (diff*scores_dict[f'1_{u}'])
            else:
                continue
        else:
            if scores[u] < 3 and u not in (1, 5):
                continue
            total += (scores[u]*scores_dict[f'1_{u}'])

    return total


dice = [5, 1, 3, 4, 1]