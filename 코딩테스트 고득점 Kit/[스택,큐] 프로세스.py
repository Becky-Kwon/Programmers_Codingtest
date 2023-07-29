# 내가 푼 코드(1시간 소요)
def solution(priorities, location):
    check = priorities[location]   #타겟값
    check_index = location        #타겟인덱스
    score = 0
    while max(priorities) > 0:
        if priorities[0] < max(priorities):        
            outback = priorities.pop(0)
            priorities.append(outback)
            check_index -=1
        else:
            if check_index == 0:
                score += 1
                break
            else :  #최고 우선순위 프로레스가 맨 앞에 있을 때
                if check_index < 0:
                    check_index = len(priorities) - abs(check_index)
                priorities.pop(0)
                score += 1
                check_index -=1
        #print('priorities : ', priorities,  "check_index : ", check_index) 
    return score

# Best 코드 (any)를 사용
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    print(queue)
    while True:
        cur = queue.pop(0)
        print(cur)
        print(queue)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
