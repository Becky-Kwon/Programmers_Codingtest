def solution(clothes):

    clo_dict = {}
    for item in clothes:
        if clo_dict.get(item[1], 0) == 0:
            clo_dict[item[1]] = 1
        else : clo_dict[item[1]] += 1
    print(clo_dict)
    answer = 1
    for k in list(clo_dict.keys()):
        answer *= (clo_dict[k]+1)
        print(answer)

    return answer-1


def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
