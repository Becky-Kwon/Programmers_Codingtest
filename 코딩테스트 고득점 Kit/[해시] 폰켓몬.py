def solution(nums):
    type_count = len(set(nums))
    if type_count >= len(nums)/2:
        answer = len(nums)/2
    else : answer = type_count 
    return answer

def solution(ls):
    return min(len(ls)/2, len(set(ls)))
